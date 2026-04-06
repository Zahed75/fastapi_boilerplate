from fastapi import APIRouter
router = APIRouter()

@router.post("/login")
async def login():
    return {"message": "Login successful"}



@router.post("/registrations")
async def registrations():
    return {"message": "Registration successful"}



@router.post("/send_otp")

async def send_otp():
    return {"message": "OTP sent successfully"}


@router.post("/set_password")
async def set_password():
    return {"message": "Password sent successfully"}




@router.post("/otp-verify")
async def otp_verify():
    return {"message": "OTP verification successful"}



@router.post("/logout")
async def logout():
    return {"message": "Logout successful"}

