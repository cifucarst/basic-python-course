set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union de los elementos
set_c = set_a.union(set_b)
# otra manera de hacer lo mismo
print(set_a | set_b) # {'col', 'mex', 'bol', 'pe', 'bol'}


# obtener los elementos en comun
set_c = set_a.intersection(set_b)
# otra manera
print(set_a & set_b)  # {'bol'}


# dejamos solo los conjuntos del conjunto a, esto es por que hace una resta
set_c = set_a.difference(set_b)
# o
print(set_a - set_b) # {'col', 'mex'}


# symetric difference => Es hacer la union de los elementos en comun
set_c = set_a.symmetric_difference(set_b)
# o
print(set_a ^ set_b) # {'col', 'mex', 'pe'}