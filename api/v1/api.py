from endpoints import auths,categories,dashboard,invoices,invoice_items,users,products

from fastapi import APIRouter
router = APIRouter()

router.include_router(auths.router,tags=["auths"])
router.include_router(categories.router,tags=["categories"])
router.include_router(dashboard.router,tags=["dashboard"])
router.include_router(invoices.router,tags=["invoices"])
router.include_router(invoice_items.router,tags=["invoice_items"])
router.include_router(users.router,tags=["users"])
router.include_router(invoices.router,tags=["invoices"])
router.include_router(invoice_items.router,tags=["invoice_items"])
router.include_router(products.router,tags=["products"])