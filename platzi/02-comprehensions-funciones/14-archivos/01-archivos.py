file = open('./text.txt')

with open('./text.txt') as file:
    for line in file:
        print(line)