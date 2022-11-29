

from decimal import Decimal
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import requests
from core.config import settings
from sql_app.models import StockMarket, User

from sql_app.session import get_db
from users.api_route import get_current_user_from_token


router = APIRouter()


@router.get("/stock-market")
def get_stock_market(
    symbol: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    apikey = settings.API_KEY
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={apikey}"
    )
    data = response.json()
    if data:
        time_series = data.get("Time Series (Daily)", None)
        if time_series:
            first_item = list(time_series.values())[0]
            second_item = list(time_series.values())[1]
            stock_market = db.query(StockMarket).filter(StockMarket.symbol == symbol).first()
            if stock_market is None:
                stock_market = StockMarket(symbol=symbol)
            stock_market.open_price = Decimal(first_item["1. open"])
            stock_market.higher_price = Decimal(first_item["2. high"])
            stock_market.lower_price = Decimal(first_item["3. low"])
            stock_market.variation_price = Decimal(first_item["4. close"]) - Decimal(second_item["4. close"])
            db.add(stock_market)
            db.commit()
            db.refresh(stock_market)
            return stock_market
    return JSONResponse(status_code=404, content={})
