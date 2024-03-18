import bcrypt
from database.models import Order, Product, User, Transaction,Notification
from database import schemas
from sqlalchemy.orm import Session

#Sao khong tao ham khoi tao :
# def __init__(self, db: Session):
#        self.db = db
#
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


def create_product(db:Session,product:schemas.ProductForCreate):
    db_product=Product(name=product.name,description=product.description,image=product.image,supplier=product.suppiler,price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
def get_product(db:Session,product_id:int):
    return db.query(Product).filter(Product.id==product_id).first()

##order
def create_order(db:Session,order:schemas.OrderForCreate):
    db_order=Order(startDate=order.startDate,endDate=order.endDate,shipToAddress=order.shipToAddress,status=order.status,totalPrice=order.totalPrice)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db:Session,order_id:int):
    return db.query(Order).filter(Order.id==order_id).first()

##Notificatrion
def create_notification(db:Session,notification:schemas.NotificationForCreate):
    db_Notification=Notification(    createOn=notification.createOn, cotent=notification.cotent)
    db.add(db_Notification)
    db.commit()
    db.refresh(db_Notification)
    return db_Notification

def get_order(db:Session,notification_id:int):
    return db.query(Notification).filter(Notification.id==notification_id).first()
