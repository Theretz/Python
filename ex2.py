number = int(input("Digite o numero a ser fatorado:  "))

resultado = 1
contador = 1

while contador <= number:
    resultado *= contador
    contador += 1

print('\nO resultado de {}! é: {} ' .format(number,resultado))