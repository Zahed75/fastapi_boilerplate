from pydantic import BaseModel

class Invoice(BaseModel):
    customer_id: int
    total:float
    discount:float
    vat:float
    payable:float

