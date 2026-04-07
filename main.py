from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from api.v1.api import router as api_router
from core.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Application")
    # create_tables()
    print("Database Created Successfully")
    yield
    print("Shutting Down Application...")




app=FastAPI(
    title="This is Fast API Boilerplate",
    description="Boilerplate-Zahed Hasan",
    docs_url="/",
    redoc_url="/redoc",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(api_router,prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Server Running "}


@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)