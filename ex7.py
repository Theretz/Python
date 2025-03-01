"""
Executar a média da lista numeros:
    .lista
    .média aritimédita 
      |-> numero
          ------
          len.numeros
"""

numero = []

numeros = [10, 20, 30, 40, 50]

numero.extend(numeros)

media = sum(numero)/len(numeros)


print(f"a média da lista {numeros} é {media}") 