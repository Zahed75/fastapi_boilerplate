from endpoints import auths,categories,dashboard,invoices,invoice_items,users,products

from fastapi import APIRouter
router = APIRouter()

router.include_router(auths.router, prefix="/auth", tags=["auths"])
router.include_router(categories.router, prefix="categories", tags=["categories"])
router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
router.include_router(invoices.router, prefix="/invoice", tags=["invoices"])
router.include_router(invoice_items.router, prefix="/invoice_item", tags=["invoice_items"])
router.include_router(users.router, prefix="users", tags=["users"])
router.include_router(invoices.router, prefix="invoice", tags=["invoices"])
router.include_router(products.router, prefix="/products", tags=["products"])