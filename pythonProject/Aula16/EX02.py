def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos_ate(numero):
    count = 0
    for i in range(2, numero + 1):
        if eh_primo(i):
            count += 1
    return count

y = 42

limite_primo = y * 2 + 5

numeros_primos = [
    numero
    for numero in range(2, limite_primo + 1)
    if eh_primo(numero)
]
soma_primos = sum(numeros_primos)

print(f"Lista de números primos: {numeros_primos}")
print(f"Soma dos números primos: {soma_primos}")
