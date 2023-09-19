valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra <= 1000:
    desconto = valor_compra * 0.10
    print(f"Desconto aplicado de 10%: R$ {desconto:.2f}")
elif valor_compra >1000 and valor_compra <= 5000:
    desconto = valor_compra * 0.20
    print(f"Desconto aplicado de 20%: R$ {desconto:.2f}")
else:
    desconto = valor_compra * 0.30
    print(f"Desconto aplicado de 30%: R$ {desconto:.2f}")

valor_final = valor_compra - desconto

print(f"Valor final da compra: R$ {valor_final:.2f}")
