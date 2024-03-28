import bcrypt
from database.models import User, Transaction
from database import schemas
from sqlalchemy.orm import Session


def do_transaction(db: Session, trans: Transaction):
    db.add(trans)
    db.query(User).\
        filter(User.id == trans.senderId).\
        update({'balance': User.balance - trans.amount})
    db.query(User).\
        filter(User.id == trans.receiverId).\
        update({'balance': User.balance - trans.amount})
    db.commit()
