lista = []

for i in range(10):
    lista.append(int(input(f"Digite o numero {i+1}: ")))

pos = 0
maior = lista[pos]

for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        pos = i

print(f"O maior numero é {maior}, e seu elemento é {pos}")
