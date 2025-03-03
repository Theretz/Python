"""
gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]
Objetivo: Quem gastou mais dinheiro. João ou Pedro
"""
joao = []

gastos_joao = [300, 500, 200, 800]

joao.extend(gastos_joao)

total_joao = sum(joao)

pedro = []

gastos_pedro = [200, 400, 500, 700]

pedro.extend(gastos_pedro)

total_pedro = sum(pedro)

if (joao > pedro):
    print ("João gastou mais dinheiro")
elif(pedro > joao):
    print("Pedro gastou mais dinheiro")
else:
    print("Os dois gastaram o mesmo dinheiro")