frase = input("Digite uma frase: ")
palavra = input("Digite a palavra: ")
qtd = frase.count(palavra)
total_palavras = frase.count(' ') + 1

print(f"A frase possui um total de {total_palavras} palavras")
print(f"A palavra {palavra} foi enocntrada {qtd} vezes na frase")
