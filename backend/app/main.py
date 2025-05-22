from fastapi import FastAPI
from app.routers import points
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api")

origins = [
    "http://localhost:8082",  # port frontendu (Vite)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # lista dozwolonych adresów
    allow_credentials=True,
    allow_methods=["*"],              # lub ["GET", "POST"] jeśli chcesz ograniczyć
    allow_headers=["*"],
)

app.include_router(points.router)