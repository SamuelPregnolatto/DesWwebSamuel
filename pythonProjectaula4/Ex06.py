
salario = float(input("insira seu salário:R$"))
percentual_aumento = float(input("insira seu percentual de aumento:"))
novo_salario = salario + ((salario * percentual_aumento) / 100)
print(f"seu novo salário é:R${novo_salario:8.2f}")