text = 'Hola, soy carlos'

unique = {c:c.upper() for c in text if c in 'aeiou'}

print(unique)