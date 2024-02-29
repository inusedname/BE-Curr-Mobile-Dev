from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import dao, models, schemas
from database.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


#----------------------------------------------------------------------------
@app.get("/users/{user_id}", response_model=schemas.UserForQuery)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = dao.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[schemas.UserForQuery])
async def get_users(db: Session = Depends(get_db)):
    return dao.get_users(db)

@app.post("/users/", response_model=schemas.UserForQuery)
async def create_user(user: schemas.UserForCreate, db: Session = Depends(get_db)):
    db_user = dao.get_user_by_phone(db, user.phone)
    if db_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    return dao.create_user(db, user)




#-----------------------T-----------------------------------------------------
@app.post("/Product/",response_model=schemas.ProductForQuery)
async def create_Product(product:schemas.ProductForCreate,db:Session=Depends(get_db)):
    return dao.create_product(db,product)
@app.get("/Product/{product_id}",response_model=schemas.ProductForQuery)
async def read_product(product_id:int,db:Session=Depends(get_db)):
    product=dao.get_product(db,product_id)
    if product is None:
         raise HTTPException(status_code=404, detail="Product not found")
    return product
@app.get("/Product/",response_model=schemas.ProductForQuery)
async def read_AllProduct(db:Session=Depends(get_db)):
    return dao.get_AllProduct(db)

@app.get("/Order/{order_id}",response_model=schemas.OrderForQuery)
async def read_order(order_id:int,db: Session = Depends(get_db)):
    order=dao.get_order(db,order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
@app.get("/Order/",response_model=schemas.OrderForQuery)
async def read_AllOrder(db: Session = Depends(get_db)):
    allOrder=dao.get_AllOrder(db)
    if allOrder is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return allOrder
@app.post("/Order/",response_model=schemas.OrderForQuery)
async def create_Order(order:schemas.UserForCreate,db:Session=Depends(get_db)):
    return dao.create_order(db,order)

