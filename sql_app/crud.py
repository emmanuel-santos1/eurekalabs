from sqlalchemy.orm import Session

from core.hashing import Hasher

from sql_app import models, schemas


# --------- USER ----------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_new_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --------- STOCK MARKET ----------
def list_stock_market(db: Session):
    stock_markets = db.query(models.StockMarket).all()
    return stock_markets

def search_stock_market(query: str, db: Session):
    stock_markets = db.query(models.StockMarket).filter(models.StockMarket.symbol.contains(query))
    return stock_markets
