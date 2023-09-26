soma = 0
qtd = int(input(f"Digite a quantidade de idades: "))
for i in range(1, qtd+1):
    n = int(input(f"entre com o {i}ª idade "))
    soma = soma + n
media = soma / qtd
print(f"A media das idades é {media:5.2f}")
