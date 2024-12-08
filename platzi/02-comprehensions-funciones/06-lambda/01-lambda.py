# lambda functions
def increment(x):
    return x + 1

result = increment(10)
# print(result)


increment_v2 = lambda x: x + 1
# print(increment_v2(20))

# /////////////////////////////////////////////////////

# otro ejemplo

full_name = lambda name, lastname: f"Mi nombre es {name.title()} y mi apellido es {lastname.title()}"

text = full_name('Nicolas', 'perez casas')
print(text)