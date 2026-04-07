from fastapi import APIRouter
router = APIRouter()


@router.post("/create_invoice_items")
async def create_invoice_items():
    return {"message": "invoice_items created successfully"}


@router.get("/get_categories")
async def read_categories():
    return {"message": "Categories retrieved successfully"}


@router.put("/invoice_items_id")
async def update_invoice_items():
    return {"message": "invoice_items updated successfully"}


@router.delete("/invoice_items_id")
async def delete_invoice_items():
    return {"message": "invoice_items deleted successfully"}
