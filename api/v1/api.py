from endpoints import auths,categories,dashboard,invoices,invoice_items,users


from fastapi import APIRouter
router = APIRouter()

router.include_router(auths.router)
router.include_router(categories.router)
router.include_router(dashboard.router)
router.include_router(invoices.router)
router.include_router(invoice_items.router)
router.include_router(users.router)
router.include_router(invoices.router)
router.include_router(invoice_items.router)