d = {}
for i in range(5):
    sobrenome = input("Digite um sobrenome: ")
    idade = int(input("Digite uma idade: "))

    d[sobrenome] = idade

maior_sobrenome = ""
maior_idade = 0

for sobrenome, idade in d.items():
    if idade > maior_idade:
        maior_idade = idade
        maior_sobrenome = sobrenome

print(f" {maior_sobrenome} é a pessoa de maior idade")
