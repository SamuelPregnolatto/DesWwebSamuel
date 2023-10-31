idade_por_sobrenome = {}
for i in range(5):
    sobrenome = input("Digite um sobrenome: ")
    idade = int(input("Digite uma idade: "))
    idade_por_sobrenome[sobrenome] = idade

idades = list(idade_por_sobrenome.values())
media_idades = sum(idades) / len(idades)
print(f"A media das idades é {media_idades}")

for sobrenome, idade in idade_por_sobrenome.items():
    if idade > media_idades:

        print(f"Sobrenome: {sobrenome}")
