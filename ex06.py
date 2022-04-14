x = int(input("Digite um número: "))
y = int(input("digite um outro número: "))
z = (x*y)+5
if z <= 0:
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"
print("Resultado final: %i. Resposta: %s" %(z,resposta))