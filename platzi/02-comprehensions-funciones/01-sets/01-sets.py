# los conjuntos no aceptan valores repetidos
set_countries = {'col', 'mex', 'bol','col'}

print(set_countries)
print(type(set_countries))


# conjunto de varios tipos
set_types = {1, 'hola', False, 12.12}

# conjunto a partir de un string
set_from_string = set('hola')

# conjunto a partir de una tupla
set_from_tuples = set(('abc','cbv','as','abc'))

# conjunto a partir de una lista
numbers = [1,2,3,4,4,3,5]
set_numbers = set(numbers)

unique_numbers = list(set_numbers)