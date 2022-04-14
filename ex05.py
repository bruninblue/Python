quantAtual = int(input("Digite a quantidade atual do estoque: "))
quantMax = int(input("Digite a quantidade máxima do estoque: "))
quantMin = int(input("Digite a quantidade mínima do estoque: "))
quantMedia = (quantMax + quantMin) / 2

if quantAtual >= quantMedia:
    print("Não efetuar compra")
else:
    print("Efetuar compra")