while True:
    base = float(input("Digite o valor da base: "))

    if base > 0:
        break
    print("O valor digitado é invalido..")
while True:
    altura = float(input("Digite o valor da altura: "))
    if altura > 0:
        break
    print("O valor digitado é invalido..")
area = (base + altura) / 2
print(f"A area do triangulo é {area:5.2f}")

