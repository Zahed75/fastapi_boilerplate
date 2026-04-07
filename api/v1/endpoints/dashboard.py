from fastapi import APIRouter
router = APIRouter()

@router.get("/dashboard")
async def get_dashboard():
    return {"message": "Dashboard"}



@router.get("/statistics")
async def get_statistics():
    return {"message": "Statistics"}


@router.get("/recentActivities")
async def get_recent_activities():
    return {"message": "Recent Activities"}


