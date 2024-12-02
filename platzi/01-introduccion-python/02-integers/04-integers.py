# funciones utiles para enteros

# abs()
print(abs(-10))  # 10
print(abs(5))    # 5

# pow()
print(pow(2, 3))        # 8
print(pow(2, 3, 3))     # 2 (calcula (2 ** 3) % 3)

# divmod()
resultado = divmod(10, 3)
print(resultado)  # (3, 1)

# conversiones
print(int(3.9))   # 3 (trunca la parte decimal)
print(bin(10))    # 0b1010
print(oct(10))    # 0o12
print(hex(10))    # 0xa