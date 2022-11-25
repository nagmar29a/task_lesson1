from pprint import pprint

stock = [
    {'name': 'iphone 12 plus', 'stock': 24, 'price': 65000,
    'recomended': ['s21', 'iphone 12']},
    {'name': 's21', 'stock': 8, 'price': 50000, 'discount': 5000},
    {'name': 'mi11', 'stock': 42, 'price': 38000}
]
pprint(stock[0]['recomended'][0])
stock[0]['recomended'].append('mi11')
stock[2]['price'] = stock[2]['price'] - 30000
pprint(stock)

print(type(stock))
print(type(stock[0]))