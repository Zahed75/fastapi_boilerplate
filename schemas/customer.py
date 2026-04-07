from pydantic import BaseModel,EmailStr

class Customer(BaseModel):
    first_name: str
    email: EmailStr
    mobile:str



class CustomerUpdate(BaseModel):
    first_name: str
    email: EmailStr
    mobile:str