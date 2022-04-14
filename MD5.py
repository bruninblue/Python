import hashlib

emailUser = hashlib.md5("12345".encode()).hexdigest()
passwUser = hashlib.md5('123456'.encode()).hexdigest()
print(emailUser)
print(passwUser)
tentativas = 3

email = hashlib.md5(input('Digite seu email: ').encode()).hexdigest()

if email != emailUser:
    print("Usuário não existe")
    tentativas = 0

if email == emailUser:
    while tentativas > 0:
        senha = hashlib.md5(input('Digite sua senha').encode()).hexdigest()
        if senha == passwUser:
            print("Acesso permitido")
            break
        else:
            print('senha errada, digite novamente')
            tentativas = tentativas - 1
            print(f"Credenciais erradas, você tem mais {tentativas} chances")

        if tentativas == 0:
            print("Acesso bloqueado")
            break
