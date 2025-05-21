from fastapi import APIRouter

router = APIRouter(
    prefix="/points",
    tags=["points"]
)

@router.get("/")
def get_point():
    return {
        "latitude": 50.3143,
        "longitude": 17.3832
    }
