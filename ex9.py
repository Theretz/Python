"""
palavras = ["python", "asimov", "código", "web", "programação"]
Objetivo: encontrar qual a maior e menor palavra com caracteres
"""

palavra = []

user = []

palavras = ["python", "asimov", "código", "web", "programação"]

palavra_user = input("Digite a lista com espaço: ").split()

palavra.extend(palavras)

user.extend(palavra_user)


maior_palavra_user = palavra_user [0]
menor_palavra_user = palavra_user [0]

maior_palavra = palavras [0]
menor_palavra = palavras [0]


for user in palavra_user:
    if len(user) > len(maior_palavra_user):
        maior_palavra_user = user 
    if len(user) < len(menor_palavra_user):
        menor_palavra_user = user 

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra 
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra 




print("A maior palavra é: ", maior_palavra)
print("A menor palavra é: ", menor_palavra)

print("A maior palavra é: ", maior_palavra_user)
print("A menor palavra é: ", menor_palavra_user)