notasAluno = {
    "nota1": '' ,
    "nota2": '',
    "media": ''
}

notasAluno['nota1'] = float(input("Digite a nota da primeira avaliação: "))
notasAluno['nota2'] = float(input("Digite a nota da segunda avaliação: "))
notasAluno['media'] = (notasAluno['nota1'] + notasAluno['nota2']) / 2

if notasAluno['media'] >= 7:
    print("O aluno está aprovado!")
    print(f"A média do aluno é {notasAluno['media']}")
else:
    print("O aluno não está aprovado")
    print(f"A média do aluno é {notasAluno['media']}")

