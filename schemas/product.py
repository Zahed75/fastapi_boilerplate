from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    price: float
    unit:str
    category_id: int
    img_url: str



class ProductUpdate(BaseModel):
    name: str
    price: float
    unit: str
    category_id: int
    img_url: str