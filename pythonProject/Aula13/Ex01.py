def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Programa de exemplo para testar a função
numero = int(input("Digite um número inteiro: "))

if eh_par(numero):
    print("O número é par (V)")
else:
    print("O número é ímpar (F)")