while True:
    valor = input("Digite os numeros: ")
    if valor.isnumeric() and len(valor) == 9:
        break
    if len(valor) != 9:
        print("Tem que ter 9 digitos")
    else:
        print("Digite apenas numeros: ")

novo_valor = valor[0] + "." + valor[1:4] + "." + valor[4:7] + "," + valor[7]+valor[8]

print(novo_valor)
