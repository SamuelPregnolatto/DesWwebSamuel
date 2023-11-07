''' Definição de Funções '''
qtd = 5
x = 10
def linha(qtd=20):
    print(qtd, "dentro", x)
    for _ in range(0,qtd):
        print("-", end='')
    print()

linha()
print(qtd, "fora", x)
print("** uso de funções **")
linha(30)