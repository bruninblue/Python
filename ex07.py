homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))

mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))

if homem1 > homem2:
    if mulher1 > mulher2:
        print(f"A soma das idades é: {homem1 + mulher2}")
        print(f"O produto das idades é: {homem2 * mulher1}")
    else:
        print(f"A soma das idades é: {homem1 + mulher1}")
        print(f"O produto das idades é: {homem2 * mulher2}")
elif homem2 > homem1:
    if mulher1 > mulher2:
        print(f"A soma das idades é: {homem2 + mulher2}")
        print(f"O produto das idades é: {homem1 * mulher1}")
    else:
        print(f"A soma da idades é: {homem2 + mulher1}")
        print(f"O produto das idades é: {homem1 * mulher2}")