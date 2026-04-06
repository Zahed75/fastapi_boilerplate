from fastapi import APIRouter
router = APIRouter()


@router.post("create_customer")
async def create_customer():
    return {"message": "customer created successfully"}


@router.get("get_categories")
async def get_categories():
    return {"message": "Categories retrieved successfully"}


@router.put("/customer_id")
async def update_customer():
    return {"message": "customer updated successfully"}


@router.delete("/customer_id")
async def delete_customer():
    return {"message": "customer deleted successfully"}