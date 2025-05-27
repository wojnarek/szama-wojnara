from pydantic import BaseModel

class Point(BaseModel):
    id: str
    name: str
    description: str
    main_category: str
    subcategories: list[str] = []
    latitude: float
    longitude: float
    google_url: str
    owner: str
    