from fastapi import FastAPI
from app.routers import points

app = FastAPI(root_path="/api")


app.include_router(points.router)