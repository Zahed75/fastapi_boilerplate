from fastapi import APIRouter
router = APIRouter()


@router.post("/create_invoices")
async def create_invoices():
    return {"message": "invoices created successfully"}


@router.get("/get_invoice")
async def get_invoice():
    return {"message": "Categories retrieved successfully"}


@router.put("/invoices_id")
async def update_invoices():
    return {"message": "invoices updated successfully"}


@router.delete("/invoices_id")
async def delete_invoices():
    return {"message": "invoices deleted successfully"}
