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
# print(population)

# Con dictionary comprehension
population_v2 = {country:random.randint(1,100) for country in countries}
# print(population_v2)



# unir dos listas
names= ['nico','zule','santi']
ages = [12, 56, 98]

# unir dos listas con zip
# print(list(zip(names, ages)))

new_dict = {name:age for (name,age) in zip(names, ages)}
print(new_dict)