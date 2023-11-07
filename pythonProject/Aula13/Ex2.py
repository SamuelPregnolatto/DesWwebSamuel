def eh_primo(numero):
    if numero <=1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# Exemplo de uso da função
numero = int(input("Digite um numero: "))

if eh_primo(numero):
    print(f"{numero} é um número primo (V)")
else:
    print(f"{numero} não é um número primo (F)")