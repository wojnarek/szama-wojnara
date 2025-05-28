from fastapi import APIRouter, HTTPException
from app.schemas.points import Point, PointDetails
from app.config import settings
import boto3

router = APIRouter(
    prefix="/points",
    tags=["points"]
)

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=settings.dynamodb_url,
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)
table = dynamodb.Table("points")



@router.get("/", response_model=list[Point])
def getAllPoints():
    try:
        response = table.scan()
        items = response.get("Items", [])
        
        points = [Point(**item) for item in items]
        return points
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{point_id}", response_model = PointDetails)
async def getPointDetails(point_id: str):
    
        response = table.get_item(
            Key={'id': point_id},
            ProjectionExpression = "id, #nme, latitude, longitude, main_category, subcategories, #own, google_url, description",
            ExpressionAttributeNames = {
                "#nme": "name", #reserved keyword nme = name
                "#own": "owner" #reserverd keyword own = owner
            }
        )
        
        item = response.get('Item')
        
        if not item:
            raise HTTPException(status_code=404, detail="Nie znaleziono punktu")
        return item
   