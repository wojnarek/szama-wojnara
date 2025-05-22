from fastapi import APIRouter
from app.schemas.points import Point

router = APIRouter(
    prefix="/points",
    tags=["points"]
)

@router.get("/", response_model=list[Point])
def getAllPoints():
    return [
        Point(latitude=50.3143, longitude=17.3832, name="Głuchołazy"),
        Point(latitude=52.2297, longitude=21.0122, name="Warszawa"),
    ]  

