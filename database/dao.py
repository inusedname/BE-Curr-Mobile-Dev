import bcrypt
from database.models import Order, OrderDetail, Product, User, Transaction
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
    db_product=Product(imgae=product.image,name=product.name,amount=product.amount)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
def get_product(db:Session, product_id:int):
    return db.query(Product).filter(Product.id==product_id).first()
def get_AllProduct(db:Session):
    products=db.query(Product).all()
    return products

def create_order(db:Session, order:schemas.OrderForCreate):
    db_order = Order(orderStatus=order.orderStatus,description=order.description,totalPrice=order.totalPrice)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
def get_order(db:Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
def get_AllOrder(db:Session):
    return db.query(Order).all()


def get_order_detail(db:Session, order_detail_id: int):
    return db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()

def create_order_detail(db:Session, order_detail:schemas.OrderDetailForCreate,order_id: int, product_id: int):
    db_order_detail = OrderDetail(dateStart=order_detail.dateStart,
        dateEnd=order_detail.dateEnd,
        quantity=order_detail.quantity,
        orderId=order_id,
        productId=product_id)
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail