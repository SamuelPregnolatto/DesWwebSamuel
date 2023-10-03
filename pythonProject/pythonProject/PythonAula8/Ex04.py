frase = input("Digite uma frase: ")
frase.lower()
vogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")

print(f"A frase possui {vogais} vogais")
