from fastapi import Depends, HTTPException

from database import schemas
from main import get_db, app
from sqlalchemy.orm import Session
from repository import user_repo
import util

@app.post("/user/login", response_model=schemas.UserForQuery)
async def login_user(user: schemas.UserForLogin, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_email(db, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    pw_hashed = util.hash(user.password)
    if db_user.password != pw_hashed:
        raise HTTPException(status_code=400, detail="Invalid password")
    # Gen JWT token and send back to user
    return db_user

@app.post("/user/signup", response_model=schemas.UserForQuery)
async def signup_user(user: schemas.UserForCreate, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repo.create_user(db, user)