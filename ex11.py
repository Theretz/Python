i = []

a = input("Digite de que número até que número de escolha").split()

for i in range(a):
    if (a%7==0 )and(a%5!=0):
        i.append(str(a))
print(i)