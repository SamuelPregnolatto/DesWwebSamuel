x = float(input("Defina o valor de x: "))
y = float(input("Defina o valor de y: "))
z = float(input("Defina o valor de z: "))

if (x < y + z) and (y < x + z) and (z < x + y):
    print(f"As medidas {x},{y} e {z} formam um triãngulo...")
    if (x == y) and (y == z):
        print("É um triângulo equilatero")
    elif (x == y) or (x == z) or (y == z):
        print("É um triângulo Isoceles")
    else:
        print("É um triângulo Escaleno")
else:
    print(f"As medidas {x},{y} e {z} não formam um triângulo")






