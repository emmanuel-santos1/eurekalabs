from fastapi import APIRouter
from users import route_users, api_route as api_route_user
from stock_market import route_stock_market, api_route as api_route_stock_market

from sql_app.session import engine
from sql_app import models

models.Base.metadata.create_all(bind=engine)

api_router = APIRouter()
api_router.include_router(route_stock_market.router, prefix="", tags=["stock-markets"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(api_route_stock_market.router, prefix="", tags=["api-stock-markets"])
api_router.include_router(api_route_user.router, prefix="", tags=["api-users"])
