k = int(input("Insira um numero maior que 1: "))
primo = True
n = 0
for i in range(1, k+1):
    if (k % i) == 0:
        n = n + 1

if n > 2:
    primo = False

if primo:
    print(f"O numero {k} é primo")
else:
    print(f"O numero {k} não é primo")
