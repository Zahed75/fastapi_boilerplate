from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Application")
    create_tables()
    print("Database Created Successfully")
    yield
    print("Shutting Down Application...")




app=FastAPI(
    title="This is FASTAPI Boilerplate",
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