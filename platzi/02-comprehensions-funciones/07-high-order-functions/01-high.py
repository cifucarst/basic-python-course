# high order functions

def increment(x):
    return x + 1


# esta es una high order function
def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2,increment)
# 2 + (2 + 1)
print(result)