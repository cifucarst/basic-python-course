dict = {}
for i in range(1,5):
    dict[i] = i * 2
# print(dict)

dict_v2 = {i:i*2 for i in range(1,5)}
# print(dict_v2)



# segundo ejemplo
import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

# Con dictionary comprehension
population_v2 = {country:random.randint(1,100)}
print(population_v2)