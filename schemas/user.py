from pydantic import BaseModel
from pydantic.v1 import EmailStr


class User(BaseModel):
    email: str
    password: str


class Register(User):
    first_name: str
    last_name: str
    email: EmailStr
    mobile: str
    password: str



class SendOTP(BaseModel):
    email: EmailStr


class VerifyOTP(BaseModel):
    email: EmailStr
    otp: int
    password: str



class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    mobile: str
    password: str

