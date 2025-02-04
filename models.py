from database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Enum, Text, TIMESTAMP, func
import enum

class CategoryEnum(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class Product(Base):
    __tablename__ = "Products"
    Product_ID = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(100))
    Category = Column(Enum(CategoryEnum))
    Description = Column(String(250))
    Product_image = Column(String(1000))
    SKU = Column(String(100))
    Unit_of_measure = Column(Enum(UnitEnum))
    Lead_time = Column(Integer)
    Created_date = Column(TIMESTAMP, server_default=func.now())
    Updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())