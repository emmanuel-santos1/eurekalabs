from sqlalchemy import Column, Integer, String, DECIMAL

from sql_app.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class StockMarket(Base):
    __tablename__ = "stock_markets"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    open_price = Column(DECIMAL)
    higher_price = Column(DECIMAL)
    lower_price = Column(DECIMAL)
    variation_price = Column(DECIMAL)
