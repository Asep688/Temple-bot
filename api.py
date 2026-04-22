import requests

BASE_URL = "https://api-testnet.templedigitalgroup.com"

def headers(api_key):
    return {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }

def get_prices(symbol, api_key):
    url = f"{BASE_URL}/api/v1/market/orderbook?symbol={symbol}&levels=1"
    res = requests.get(url, headers=headers(api_key)).json()

    ob = res["orderbook"]
    market = (ob["best_bid"] + ob["best_ask"]) / 2
    oracle = res.get("oracle_price", market)

    return market, oracle


def get_balance(api_key):
    url = f"{BASE_URL}/api/v1/account/balance"
    return requests.get(url, headers=headers(api_key)).json()


def get_rewards(api_key):
    url = f"{BASE_URL}/api/v1/account/rewards"
    try:
        return requests.get(url, headers=headers(api_key)).json()
    except:
        return {"reward": "N/A"}


def place_order(symbol, side, price, amount, api_key):
    url = f"{BASE_URL}/api/trading/orders"

    payload = {
        "symbol": symbol,
        "side": side,
        "price": price,
        "quantity": amount,
        "order_type": "limit"
    }

    return requests.post(url, json=payload, headers=headers(api_key)).json()


def get_orders(api_key):
    url = f"{BASE_URL}/api/trading/orders"
    return requests.get(url, headers=headers(api_key)).json()
