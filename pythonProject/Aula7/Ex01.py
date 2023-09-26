N = int(input("Digite um valor inteiro e positivo N: "))

E = 0

for i in range(1, N + 1):

    E = E + (2**i)

print(f"O valor de E é: {E}")
