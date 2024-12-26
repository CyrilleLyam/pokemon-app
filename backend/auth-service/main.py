from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr
import argon2
from datetime import timedelta, datetime
from jwt import encode as jwt_encode
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

ph = argon2.PasswordHasher()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
PORT = int(os.getenv("PORT"))

mock_users = [
    {
        "email": "john.doe@example.com",
        "username": "John Doe",
        "password": ph.hash("password123"),
        "avatar": "https://robohash.org/johndoe.png"
    },
    {
        "email": "jane.smith@example.com",
        "username": "Jane Smith",
        "password": ph.hash("securePass456"),
        "avatar": "https://robohash.org/janesmith.png"
    },
    {
        "email": "seanglay.sq@outlook.com",
        "username": "Seanglay",
        "password": ph.hash("seanglaypassword"),
        "avatar": "https://avatars.githubusercontent.com/u/65019603?v=4"
    }
]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt_encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login")
def login_user(user: UserLogin, response: Response):
    user_data = next((u for u in mock_users if u["email"] == user.email), None)
    if not user_data:
        raise HTTPException(status_code=404, detail="USER_NOT_FOUND")
    try:
        if ph.verify(user_data["password"], user.password):
            access_token = create_access_token({"sub": user.email})
            response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
            return {
                "message": "LOGIN_SUCCESSFUL"
            }
    except argon2.exceptions.VerifyMismatchError:
        raise HTTPException(status_code=401, detail="INVALID_CREDENTIALS")

    raise HTTPException(status_code=401, detail="INVALID_CREDENTIALS")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("__main__:app", host="0.0.0.0", port=PORT, reload=True)
