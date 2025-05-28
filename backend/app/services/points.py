import boto3
import pydantic
from app.config import settings
from app.schemas.points import Point, PointDetails

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=settings.dynamodb_url,
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

point_table = dynamodb.Table("points")

user_table = dynamodb.Table("users")

def getAllPointsFromDB():
        response = point_table.scan()
        
        items = response.get("Items",[])
        
        points = [Point(**item) for item in items]
        
        return points


def getPointDetailFromDB(point_id: str):
    
    response = point_table.get_item(
        Key={'id': point_id},
        ProjectionExpression = "id, #nme, latitude, longitude, main_category, subcategories, #own, google_url, description",
            ExpressionAttributeNames = {
                "#nme": "name", #reserved keyword nme = name
                "#own": "owner" #reserverd keyword own = owner
            }
    )
    
    item = response.get('Item')
    
    return item
    
    