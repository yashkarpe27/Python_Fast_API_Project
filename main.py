from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Product
from schemas import ProductCreate, ProductResponse
from typing import List

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=List[ProductResponse])
def list_products(page: int=1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    Products = db.query(Product).offset(offset).limit(limit).all()
    return Products

@app.get("/products/{pid}/info", response_model=ProductResponse)
def get_product(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.Product_ID == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return product

@app.post("/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_data = product.dict()
    product_data['product_image'] = str(product.Product_image)
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.Product_ID == pid).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail='Product Not Found')
    
    for key, value in product.dict().items():
        setattr(existing_product, key, value)
    
    db.commit()
    db.refresh(existing_product)
    return existing_product