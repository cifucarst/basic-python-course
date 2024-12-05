price = 100

def increment():
    global price
    price = price + 10
    print(price)

print(price)

increment()