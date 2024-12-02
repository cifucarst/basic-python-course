# aplicaciones practicas

# par o impar
def es_par(n):
    return n % 2 == 0

print(es_par(4))  # True
print(es_par(7))  # False


# Encontrar el maximo comun divisor
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(mcd(48, 18))  # 6


# conversion entre bases

def convertir_bases(n):
    return {
        "binario": bin(n),
        "octal": oct(n),
        "hexadecimal": hex(n)
    }

print(convertir_bases(255))
# {'binario': '0b11111111', 'octal': '0o377', 'hexadecimal': '0xff'}