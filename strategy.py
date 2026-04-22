from config import CONFIG


def calculate_prices(oracle):
    buy_price = oracle * (1 + CONFIG["buy_offset"])
    sell_price = oracle * (1 + CONFIG["sell_offset"])
    return buy_price, sell_price


def validate(buy, sell):
    return buy < sell


def should_trade(market, oracle):
    return abs(market - oracle) >= CONFIG["min_deviation"]
