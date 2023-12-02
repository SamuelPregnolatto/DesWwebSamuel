from datetime import datetime
import calendar

def valida_data(data_nascimento):
    formato_data = "%d/%m/%Y"
    partes_data = data_nascimento.split('/')

    if len(partes_data) == 3:
        dia, mes, ano = map(int, partes_data)

        if 1900 <= ano <= 9999 and 1 <= mes <= 12 and 1 <= dia <= calendar.monthrange(ano, mes)[1]:
            hoje = datetime.now()

            data_formatada = datetime(ano, mes, dia)
            idade_minima = (hoje - data_formatada).days >= 365 * 18

        return idade_minima

    return False

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

if valida_data(data_nascimento):
    print("A data é válida e a pessoa tem 18 anos ou mais.")
else:
    print("A data não é válida ou a pessoa tem menos de 18 anos.")
