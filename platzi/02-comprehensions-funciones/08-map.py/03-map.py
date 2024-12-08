items  = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    },
]

prices = list(map(lambda x: x['price'], items))
# print(prices)

# //////////////////////////////////////////////////////////////

# aca estamos realizando una mutacion en el array original
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))

print(new_items)