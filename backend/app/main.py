from fastapi import FastAPI
from app.routers import points
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(root_path="/api")

origins = os.getenv("CORS_ORIGINS", "")
origins = [o.strip() for o in origins.split(",") if o.strip()]

print(f"CORS_ORIGINS loaded from .env: {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*"],
)

app.include_router(points.router)