from pydantic import BaseModel, EmailStr
from typing import Optional

# Incoming payload when registering
class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

# Incoming payload when logging in
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# What we return on a successful login
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# Example of a user object we might return
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr