numbers = [1,2,3,4,5]

numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)

# print(numbers_v2)

squares = list(map(lambda x: x*2,numbers))
print(squares)