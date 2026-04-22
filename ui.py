def show_ui(name, balance, reward, market, oracle, buy, sell, orders, status):
    print("\n==============================")
    print("Temple Bot Dashboard")
    print("==============================\n")

    print(f"Account: {name}")
    print(f"Balance: {balance}")
    print(f"Reward : {reward}\n")

    print(f"Market : {round(market,6)}")
    print(f"Oracle : {round(oracle,6)}\n")

    print(f"Buy    : {round(buy,6)}")
    print(f"Sell   : {round(sell,6)}\n")

    print("Status :")
    for s in status:
        print(f"[✓] {s}")

    print("\nOrders:")
    for o in orders:
        side = o.get("side")
        price = o.get("price")
        state = o.get("status", "unknown")
        print(f"- {side.upper()} {price} ({state})")

    print("\n==============================")
