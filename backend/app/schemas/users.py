from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    access_code: str
    
class UserNameAndId(BaseModel):
    id: str
    username: str