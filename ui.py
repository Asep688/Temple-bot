def show_ui(name, balance, reward, market, oracle, buy, sell, orders, status):
    print("\n==============================")
    print("Temple Bot Dashboard")
    print("==============================\n")

    print(f"Account: {name}")
    print(f"Balance: {balance}")
    print(f"Reward : {reward}\n")

    print(f"Market : {market}")
    print(f"Oracle : {oracle}\n")

    print(f"Buy    : {buy}")
    print(f"Sell   : {sell}\n")

    print("Status :")
    for s in status:
        print(f"[✓] {s}")

    print("\nOrders:")
    if isinstance(orders, list):
        for o in orders:
            side = o.get("side", "?")
            price = o.get("price", "?")
            state = o.get("status", "unknown")
            print(f"- {side.upper()} {price} ({state})")
    else:
        print(orders)

    print("\n==============================")
