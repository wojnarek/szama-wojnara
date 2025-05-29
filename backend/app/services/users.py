import boto3
from app.config import settings
from boto3.dynamodb.conditions import Key
from app.schemas.users import User

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=settings.dynamodb_url,
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

user_table = dynamodb.Table("users")


def getUsernameById(user_id: str):
    
    
    response = user_table.get_item(
        Key={'id': user_id},
        ProjectionExpression = "id, username"
    )
    
    item = response.get('Item')
    
    print(f"user z bazy: {item}")
    
    return item

def checkAccesCode(code: str):

    response = user_table.query(
        IndexName='AccessCode',
        KeyConditionExpression=Key('access_code').eq(code)
    )
    items = response.get('Items', [])
    if items:
        return items[0]
    else:
        return None