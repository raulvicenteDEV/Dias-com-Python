total = float(input("Informe o valor da compra: "))  # Aceita valores decimais

#total = compra - (compra * 0.05)

# Aplica os descontos adicionais
if total > 200:
    total -= total * 0.21  # Aplica 20% de desconto
    print(f"Desconto de 20% aplicado. Total final: R$ {total:.2f}")
elif total > 100:
    total -= total * 0.1  # Aplica 10% de desconto
    print(f"Desconto de 10% aplicado. Total final: R$ {total:.2f}")
else:
    print("sem desconto")