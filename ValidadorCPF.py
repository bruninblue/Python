cpf = input("Digite seu cpf (11 dígitos)?")
novo_cpf = ''
valor1 = 0
valor2 = 0

for ind, dig in enumerate(range(10, 1, -1)):
    valor1 += int(cpf[ind]) * dig

# print(valor1)

for ind, dig in enumerate(range(11, 1, -1)):
    valor2 += int(cpf[ind]) * dig

# print(valor2)

valor1 = 11 - (valor1 % 11)
valor2 = 11 - (valor2 % 11)

# print(valor1, valor2)

if valor1 > valor2:
    # print(cpf[9], cpf[10])
    for ind in range(11):
        novo_cpf += cpf[ind]

if novo_cpf == cpf:
    print("CPF válido")
    print(type(novo_cpf))
else:
    print("CPF inválido!")

