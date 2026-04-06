from fastapi import APIRouter
router = APIRouter()


@router.post("create_category")
async def create_category():
    return {"message": "Category created successfully"}


@router.get("get_categories")
async def get_categories():
    return {"message": "Categories retrieved successfully"}


@router.put("/category_id")
async def update_category():
    return {"message": "Category updated successfully"}


@router.delete("/category_id")
async def delete_category():
    return {"message": "Category deleted successfully"}