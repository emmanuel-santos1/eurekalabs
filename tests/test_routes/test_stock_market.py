import time
import pytest
import responses

from core.config import settings
from tests.utils.stock_market import external_data_from_prices, external_data_unknown_symbol


@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1.5)


@responses.activate
def test_read_stock_market(client, normal_user_token_headers):
    symbol = "IBM"
    data = external_data_from_prices(symbol, "12.5", "13.8", "12.3", "12.6", "12.5")
    responses.add(responses.GET, f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={settings.API_KEY}",
                json=data, status=200)
    response = client.get(
        f"/stock-market?symbol={symbol}", headers=normal_user_token_headers
    )
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["symbol"] == symbol
    assert json_response["open_price"] == 12.5
    assert json_response["higher_price"] == 13.8
    assert json_response["lower_price"] == 12.3
    assert json_response["variation_price"] == 0.1

@responses.activate
def test_read_stock_market_fail(client, normal_user_token_headers):
    symbol = "UNKNOW"
    data = external_data_unknown_symbol(symbol)
    responses.add(responses.GET, f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={settings.API_KEY}",
                json=data, status=200)
    response = client.get(
        f"/stock-market?symbol={symbol}", headers=normal_user_token_headers
    )
    assert response.status_code == 404
