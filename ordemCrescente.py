numOrdemCresc = []
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
valor3 = int(input("Digite outro valor: "))

if valor1 < valor2 and valor2 < valor3:
    numOrdemCresc = [valor1, valor2, valor3]
elif valor1 < valor3 and valor3 < valor2:
    numOrdemCresc = [valor1, valor3, valor2]
elif valor2 < valor1 and valor1 < valor3:
    numOrdemCresc = [valor2, valor1, valor3]
elif valor2 < valor3 and valor3 < valor2:
    numOrdemCresc = [valor2, valor3, valor1]
elif valor3 < valor1 and valor1 < valor2:
    numOrdemCresc = [valor3, valor1, valor2]
# elif valor3 < valor2 and valor2 < valor1:
else:
    numOrdemCresc = [valor3, valor2, valor1]

print(numOrdemCresc)

#valor1 valor2 valor3 v
#valor1 valor3 valor2 v
#valor2 valor1 valor3 v
#valor2 valor3 valor1 v
#valor3 valor1 valor2 v
#valor3 valor2 valor1 v   