data = (input("Insira uma data no formato DD/MM/AAAA: "))

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print(f"{ano}{mes}{dia}")
