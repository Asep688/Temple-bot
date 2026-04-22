import time
import random

from config import CONFIG
from accounts import ACCOUNTS
import api
import strategy
import ui


def run_account(account):
    name = account["name"]
    key = account["api_key"]

    market, oracle = api.get_prices(CONFIG["symbol"], key)

    if market is None:
        print("Skip karena data error")
        return

    if not strategy.should_trade(market, oracle):
        print("Skip: market dekat oracle")
        return

    buy, sell = strategy.calculate_prices(oracle)

    if not strategy.validate(buy, sell):
        print("Skip: invalid spread")
        return

    status = []

    buy_tx = api.place_order(CONFIG["symbol"], "buy", buy, CONFIG["amount"], key)
    sell_tx = api.place_order(CONFIG["symbol"], "sell", sell, CONFIG["amount"], key)

    if "error" not in str(buy_tx):
        status.append("Buy Order Sent")
    if "error" not in str(sell_tx):
        status.append("Sell Order Sent")

    balance = api.get_balance(key)
    reward = api.get_rewards(key)
    orders = api.get_orders(key)

    ui.show_ui(name, balance, reward, market, oracle, buy, sell, orders, status)


def main():
    while True:
        try:
            for acc in ACCOUNTS:
                run_account(acc)

            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print("FATAL ERROR:", e)


if __name__ == "__main__":
    main()
