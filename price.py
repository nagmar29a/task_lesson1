def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

net_price = format_price(56.24)
print(net_price)