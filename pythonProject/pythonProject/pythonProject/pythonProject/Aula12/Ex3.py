lista1 = []
lista2 = []
for i in range(5):
    valor = int(input(f"Insira o {i + 1}º valor da primeira lista: "))
    lista1.append(valor)

for i in range(5):
    valor = int(input(f"Insira o {i + 1}º valor da segunda lista: "))
    lista2.append(valor)

conjunto_uniao = set(lista1).union(lista2)

print("O conjunto da união entre as duas listas é: ", conjunto_uniao)

