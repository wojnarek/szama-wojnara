from pydantic import BaseModel

class Point(BaseModel):
    id: str
    name: str
    main_category: str
    subcategories: list[str] = []
    latitude: float
    longitude: float

class PointDetails(BaseModel):
    id: str
    name: str
    description: str
    main_category: str
    subcategories: list[str] = []
    latitude: float
    longitude: float
    google_url: str
    owner: str
    owner_name: str
    
    
class NewPoint(BaseModel):
    name: str
    description: str
    main_category: str
    subcategories: list[str] = []
    latitude: float
    longitude: float
    access_code: str
    
    