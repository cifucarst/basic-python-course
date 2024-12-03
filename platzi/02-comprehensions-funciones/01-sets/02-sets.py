# crud con sets

set_coutries = {'col', 'mex','bol'}

# ver el tamano del conjunto
size = len(set_coutries)

# verificar si cierto valor esta en el conjunto
print('col' in set_coutries) # True
print('pe' in set_coutries) # False


# agregar un elemento
set_coutries.add('pe')


# update - lo que hace es sumar elementos a los existentes
set_coutries.update({'ar','ecua','pe'})


# remove
set_coutries.remove('col')

# otra manera de eliminar, si no esta no genera errores
set_coutries.discard('arg')

# limpiar todo el conjunto, dejarlo vacio
set_coutries.clear()