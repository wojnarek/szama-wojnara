import boto3
from uuid import uuid4
from config import settings
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=settings.dynamodb_url,
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)
user_table = dynamodb.Table('users')  

def add_user():
    username = input("Podaj username: ").strip()
    access_code = input("Podaj access code: ").strip()
    user_id = str(uuid4())

    user_item = {
        'id': user_id,
        'username': username,
        'access_code': access_code
    }

    print("Dodaję użytkownika:", user_item)

    try:
        user_table.put_item(Item=user_item)
        print("✅ Użytkownik został dodany do bazy!")
    except Exception as e:
        print("❌ Błąd podczas dodawania użytkownika:", e)

if __name__ == "__main__":
    add_user()
