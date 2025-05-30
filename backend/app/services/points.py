import boto3
import pydantic
from app.config import settings
from app.schemas.points import Point, PointDetails, NewPoint
from app.services.users import getUsernameById
from app.schemas.users import User
from uuid import uuid4
from decimal import Decimal

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=settings.dynamodb_url,
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

point_table = dynamodb.Table("points")


def getAllPointsFromDB():
        response = point_table.scan()
        
        items = response.get("Items",[])
        
        points = [Point(**item) for item in items]
        
        return points


def getPointDetailFromDB(point_id: str):
    
    response = point_table.get_item(
        Key={'id': point_id},
        ProjectionExpression = "id, #nme, latitude, longitude, main_category, subcategories, #own, google_url, description, owner_name",
            ExpressionAttributeNames = {
                "#nme": "name", #reserved keyword nme = name
                "#own": "owner" #reserverd keyword own = owner
            }
    )
    
    item = response.get('Item')
        
    user = getUsernameById(item['owner'])
    
    if user:
        item['owner_name'] = user['username']
    else:
        item['owner_name'] = 'siakalaka'
    
    return item
    

def addNewPointToDB(newPoint: NewPoint, user: dict):
    
    point_id = str(uuid4())
    
    url = f"https://maps.google.com/?q={newPoint.latitude},{newPoint.longitude}"
        
    point = {
        'id': point_id,
        'name': newPoint.name,
        'description': newPoint.description,
        'main_category': newPoint.main_category,
        'subcategories': newPoint.subcategories,
        'latitude': Decimal(str(newPoint.latitude)),
        'longitude': Decimal(str(newPoint.longitude)),
        'google_url': url,
        'owner': user['id'],
        'owner_name': user['username']
        }
    
    point_table.put_item(Item=point)
    
    return point
    