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

    balance = api.get_balance(key)
    reward = api.get_rewards(key)

    market, oracle = api.get_prices(CONFIG["symbol"], key)

    if not strategy.should_trade(market, oracle):
        return

    buy_price, sell_price = strategy.calculate_prices(oracle)

    if not strategy.validate(buy_price, sell_price):
        return

    status = []

    buy_tx = api.place_order(CONFIG["symbol"], "buy", buy_price, CONFIG["amount"], key)
    sell_tx = api.place_order(CONFIG["symbol"], "sell", sell_price, CONFIG["amount"], key)

    if buy_tx:
        status.append("Buy Order Sent")
    if sell_tx:
        status.append("Sell Order Sent")

    orders = api.get_orders(key)

    ui.show_ui(
        name,
        balance,
        reward,
        market,
        oracle,
        buy_price,
        sell_price,
        orders,
        status
    )


def main():
    while True:
        try:
            for acc in ACCOUNTS:
                run_account(acc)

            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print("ERROR:", e)


if __name__ == "__main__":
    main()
