from fastapi import APIRouter, HTTPException
from app.schemas.points import Point, PointDetails
from app.config import settings
from app.services.points import getAllPointsFromDB
from app.services.points import getPointDetailFromDB
from app.services.users import getUsernameById
from app.schemas.users import UserNameAndId

router = APIRouter(
    prefix="/points",
    tags=["points"]
)


@router.get("/", response_model=list[Point])
def getAllPoints():
    if not getAllPointsFromDB():
        raise HTTPException(status_code=404, detail="Brak punktów")
    return getAllPointsFromDB()


@router.get("/{point_id}", response_model = PointDetails)
async def getPointDetails(point_id: str):
        if not getPointDetailFromDB(point_id):
            raise HTTPException(status_code=404, detail="Nie znaleziono punktu")
        return getPointDetailFromDB(point_id)
   