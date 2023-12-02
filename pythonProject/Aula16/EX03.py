def processar_numero(numero_ra):
    soma_digitos = 0
    multiplicacao_digitos = 1

    for digito_str in numero_ra:
        digito_ra = int(digito_str)
        soma_digitos += digito_ra
        multiplicacao_digitos *= digito_ra

    return soma_digitos, multiplicacao_digitos

numero_ra = input("Digite o numero do seu RA: ")

soma_ra, multiplicacao_ra= processar_numero(numero_ra)

print(f"A soma dos dígitos do seu RA é: {soma_ra}")
print(f"A multiplicação dos dígitos do seu RA é: {multiplicacao_ra}")

