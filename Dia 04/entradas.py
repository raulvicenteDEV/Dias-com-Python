# Mutiplas entradas na mesma linha de input()

dados =input('Digite o seu nome e sua idade: ').split()
nome = dados[0]
idade = dados[1]

print(f"Meu nome é {nome.upper()} e tenho {idade} anos de idade")