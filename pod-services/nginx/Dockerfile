FROM openresty/openresty:buster

# Install dependencies
RUN apt-get update && apt-get install -y \
  curl \
  build-essential \
  libreadline-dev \
  unzip \
  wget \
  libssl-dev \
  && apt-get clean

# Install LuaRocks from source
RUN wget https://luarocks.github.io/luarocks/releases/luarocks-3.9.2.tar.gz && \
  tar zxpf luarocks-3.9.2.tar.gz && \
  cd luarocks-3.9.2 && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -rf luarocks-3.9.2 luarocks-3.9.2.tar.gz

# Install lua-resty-jwt
RUN luarocks install lua-resty-jwt
