pesos = 0
alturas = 0
maior_imc = 0
menor_imc = 0
for i in range(1, 6):

    peso = float(input(f"Pessoa {1}: Peso: "))
    altura = float(input(f"Pessoa {1}: altura: "))
    pesos = pesos + peso
    alturas = alturas + altura
    imc = peso / (altura * altura)
    if maior_imc == 0:
        maior_imc = imc
        menor_imc = imc
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
media_peso = pesos / 5
media_altura = alturas / 5
print (f"Peso Médio..: {media_peso:5.2f}")
print (f"Altura Média..: {media_altura:5.2f}")
print (f"Peso Médio..: {media_peso:5.2f}")
print (f"Peso Médio..: {media_peso:5.2f}")