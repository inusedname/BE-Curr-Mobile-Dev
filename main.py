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