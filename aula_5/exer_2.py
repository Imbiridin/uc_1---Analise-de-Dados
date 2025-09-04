'''2) Uma empresa almeja um programa que fará a leitura de 5 produtos e no final irá exibir apenas
o somatório dos produtos que custam acima de 200 reais.'''

# Exercício 2

soma = 0

for i in range(5):
    
    valor_p = float(input("Digite o valor do produto: "))
    
    if valor_p >= 200:
        soma += valor_p

print(f"A soma dos produtos acima de 200 reais é: {soma:.2f}")
    