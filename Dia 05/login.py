user = "admin"
senha = "123456"

usuario = input("Digite o nome do usuario: ")
senha2 = input("Digite sua senha: ")

if user == usuario and senha2 == senha:
    print("Login encontrado")

else:
    print("usuario ou senha erradas")
