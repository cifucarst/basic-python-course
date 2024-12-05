def sum_with_rage(min,max):
    result = 0
    for i in range(min,max):
        result += i
    return result

def my_print():
    print(sum_with_rage(1,10))

my_print()