import boto3
from app.config import settings
import boto3
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
    print(f"user id to: {user_id}")
    response = user_table.get_item(
        Key={'id': user_id},
        ProjectionExpression = "id, username"
    )
    
    item = response.get('Item')
    
    print(f"user z bazy: {item}")
    
    return item