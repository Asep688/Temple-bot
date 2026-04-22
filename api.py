import requests

BASE_URL = "https://api-testnet.templedigitalgroup.com"


def headers(api_key):
    return {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }


# =========================
# GET PRICE (SUPER SAFE)
# =========================
def get_prices(symbol, api_key):
    url = f"{BASE_URL}/api/v1/market/orderbook?symbol={symbol}&levels=1"

    res = requests.get(url, headers=headers(api_key))
    
    try:
        data = res.json()
    except:
        print("❌ Response bukan JSON:", res.text)
        return None, None

    print("DEBUG RESPONSE:", data)  # 🔥 WAJIB (hapus nanti kalau sudah stabil)

    try:
        # FORMAT 1
        if "orderbook" in data:
            ob = data["orderbook"]
            best_bid = float(ob["best_bid"])
            best_ask = float(ob["best_ask"])

        # FORMAT 2
        elif "bids" in data and "asks" in data:
            best_bid = float(data["bids"][0][0])
            best_ask = float(data["asks"][0][0])

        # FORMAT 3
        elif "data" in data:
            ob = data["data"]
            best_bid = float(ob["bids"][0][0])
            best_ask = float(ob["asks"][0][0])

        else:
            print("❌ Format tidak dikenal")
            return None, None

        market = (best_bid + best_ask) / 2
        oracle = data.get("oracle_price", market)

        return market, oracle

    except Exception as e:
        print("❌ ERROR parsing:", e)
        print("DATA:", data)
        return None, None


# =========================
# BALANCE
# =========================
def get_balance(api_key):
    try:
        url = f"{BASE_URL}/api/v1/account/balance"
        return requests.get(url, headers=headers(api_key)).json()
    except:
        return "ERROR"


# =========================
# REWARD
# =========================
def get_rewards(api_key):
    try:
        url = f"{BASE_URL}/api/v1/account/rewards"
        return requests.get(url, headers=headers(api_key)).json()
    except:
        return "N/A"


# =========================
# ORDER
# =========================
def place_order(symbol, side, price, amount, api_key):
    url = f"{BASE_URL}/api/trading/orders"

    payload = {
        "symbol": symbol,
        "side": side,
        "price": price,
        "quantity": amount,
        "order_type": "limit"
    }

    try:
        return requests.post(url, json=payload, headers=headers(api_key)).json()
    except:
        return {"error": "order failed"}


def get_orders(api_key):
    try:
        url = f"{BASE_URL}/api/trading/orders"
        return requests.get(url, headers=headers(api_key)).json()
    except:
        return []
