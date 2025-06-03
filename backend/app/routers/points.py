from fastapi import APIRouter, HTTPException
from app.schemas.points import Point, PointDetails, NewPoint
from app.config import settings
from app.services.points import getAllPointsFromDB
from app.services.points import getPointDetailFromDB, addNewPointToDB
from app.services.users import checkAccesCode
from app.schemas.users import UserNameAndId, User
from uuid import uuid4

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
   
   
@router.post("/", response_model=PointDetails)
async def addNewPoint(newPoint: NewPoint):

    print(f"{newPoint}")

    user = checkAccesCode(newPoint.access_code)
    
    if not user:
        raise HTTPException(status_code=401, detail="Niepoprawny kod dostępu!")
    newPointFromDb = addNewPointToDB(newPoint, user)
    
    print(f"nowy punkt: {newPointFromDb}")
        
    return PointDetails(**newPointFromDb)

@router.get("/health")
async def health_check():
    return {"status": "ok"}
    