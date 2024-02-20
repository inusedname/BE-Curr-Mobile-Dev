import bcrypt
from database.models import User, Transaction
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: User):
    hashed = bcrypt.hashpw(user.pw, bcrypt.gensalt())
    user.pw = hashed
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def do_transaction(db: Session, trans: Transaction):
    db.add(trans)
    db.query(User).\
        filter(User.id == trans.senderId).\
        update({'balance': User.balance - trans.amount})
    db.query(User).\
        filter(User.id == trans.receiverId).\
        update({'balance': User.balance - trans.amount})
    db.commit()
