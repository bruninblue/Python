salarioFixo = int(input("Informe o salário fixo do funcionário: "))
valorVendas = int(input("Informe o valor de vendas realizadas pelo funcionário: "))
comissao = 0

if valorVendas <= 1500:
    comissao = (valorVendas / 100) * 3
    print(f"O valor total do salário do funcionário é R${salarioFixo + comissao} reais")
else:
    comissao = (valorVendas / 100) * 5
    print(f"O valor total do salário do funcionário é R${salarioFixo + comissao} reais")
 