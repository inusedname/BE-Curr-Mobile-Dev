import bcrypt
from database.models import User, Transaction
from database import schemas
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserForCreate):
    hashed = bcrypt.hashpw(user.pw.encode('utf-8'), bcrypt.gensalt())
    user.pw = hashed
    db_user = User(phone=user.phone, pw=user.pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def do_transaction(db: Session, trans: Transaction):
    db.add(trans)
    db.query(User).\
        filter(User.id == trans.senderId).\
        update({'balance': User.balance - trans.amount})
    db.query(User).\
        filter(User.id == trans.receiverId).\
        update({'balance': User.balance - trans.amount})
    db.commit()
