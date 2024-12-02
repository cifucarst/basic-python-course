# operaciones con operadores avanzados

a = 0b1100  # 12 en binario
b = 0b1010  # 10 en binario

print(bin(a & b))  # 0b1000 (AND)
print(bin(a | b))  # 0b1110 (OR)
print(bin(a ^ b))  # 0b0110 (XOR)
print(bin(~a))     # -0b1101 (NOT)
print(bin(a << 2)) # 0b110000 (desplaza 2 bits a la izquierda)
print(bin(a >> 2)) # 0b0011 (desplaza 2 bits a la derecha)

