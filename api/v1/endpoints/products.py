from fastapi import APIRouter
router = APIRouter()

@router.post("/create_product")
async def create_product():
    return {"message": "product created successfully"}


@router.get("/update_product")
async def update_product():
    return {"message": "product updated successfully"}


@router.get("/get_products")
async def get_products():
    return {"message": "products retrieved successfully"}
