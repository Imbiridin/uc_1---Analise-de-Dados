valor = int(input("Digite o valor que você quer fazer:"))
parcelas = int(input("Digite o número de parcelas que você deseja realizar:"))

total = valor / parcelas

print(f"\nO valor é de: {valor}.\nAs parcelas são de: {parcelas}.\nO total é de: {total:.2f}.\n")
