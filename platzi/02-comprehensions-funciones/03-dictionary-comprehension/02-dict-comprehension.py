# dictionary comprehension: condition

import random


countries = ['col', 'mex', 'bol', 'pe']

population = {country:random.randint(1,100) for country in countries}
print(population)

# diccionario con la condicion
result = {country: population for (country, population) in population.items() if population > 20}
print(result)