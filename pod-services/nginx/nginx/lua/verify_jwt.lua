local function load_env(file_path)
    local env_vars = {}
    local file = io.open(file_path, "r")
    if not file then return env_vars end
    for line in file:lines() do
        local key, value = line:match("^([%w_]+)=(.+)$")
        if key and value then env_vars[key] = value end
    end
    file:close()
    return env_vars
end

local env = load_env("/etc/nginx/lua/.env")

local jwt = require "resty.jwt"
local cookie = ngx.var.http_cookie
local token = cookie and ngx.re.match(cookie, 'access_token=([^;]+)')

if not token or not token[1] then
    ngx.status = ngx.HTTP_UNAUTHORIZED
    ngx.say("Missing or invalid token")
    return ngx.exit(ngx.HTTP_UNAUTHORIZED)
end

local raw_token = ngx.unescape_uri(token[1])
raw_token = raw_token:gsub('^"', ''):gsub('"$', '')
local token_value = raw_token:match("^Bearer%s+(.+)$") or raw_token

local SECRET_KEY = env["SECRET_KEY"]
if not SECRET_KEY then
    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
    ngx.say("Server configuration error: SECRET_KEY is missing")
    return ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
end

local jwt_obj = jwt:verify(SECRET_KEY, token_value)

if not jwt_obj.verified then
    ngx.status = ngx.HTTP_UNAUTHORIZED
    ngx.say("Invalid token: ", jwt_obj.reason)
    return ngx.exit(ngx.HTTP_UNAUTHORIZED)
end

if jwt_obj.payload.exp and os.time() > jwt_obj.payload.exp then
    ngx.status = ngx.HTTP_UNAUTHORIZED
    ngx.say("Token has expired")
    return ngx.exit(ngx.HTTP_UNAUTHORIZED)
end
