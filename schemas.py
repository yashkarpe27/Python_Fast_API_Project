from pydantic import BaseModel, Field
from models import CategoryEnum, UnitEnum
from datetime import datetime
class ProductCreate(BaseModel):
    Name: str
    Category: CategoryEnum
    Description: str
    Product_image: str = Field(..., pattern="^https?://.*")
    SKU: str
    Unit_of_measure: UnitEnum
    Lead_time: int = Field(..., gt=0, le=999)

class ProductResponse(ProductCreate):
    Product_ID: int
    Created_date: datetime
    Updated_date: datetime

    class config:
        orm_mode = True