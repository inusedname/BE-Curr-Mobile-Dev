
from database import database
from sqlalchemy import Column, Integer, String, Float


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True)
    pw = Column(String)

class Transaction(database.Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    senderId = Column(Integer)
    receiverId = Column(Integer)
    amount = Column(Float, default=0.0)
