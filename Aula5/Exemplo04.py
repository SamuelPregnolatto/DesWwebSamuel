dia = int(input("Entre com o numero do dia: "))

match dia:
    case 1:
        nome = "Domingo"
    case 2:
        nome = "Segunda-Feira"
    case 3:
        nome = "Terça-Feira"
    case 4:
        nome = "Quarta-Feira"
    case 5:
        nome = "Quinta-Feira"
    case 6:
        nome = "Setxa-Feira"
    case 7:
        nome = "Sábado"
    case _:
        nome = f"Valor {dia} è invalido"

print(nome)
