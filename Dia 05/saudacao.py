horario = float(input("Me informe o horario da mensagem: "))
nome = str(input("Informe seu nome: "))

if horario <= 12:
    print(f"Bom dia {nome}")

elif horario <= 18:
    print(f"Boa tarde {nome}")

else:
    print(f"Boa noite {nome}")