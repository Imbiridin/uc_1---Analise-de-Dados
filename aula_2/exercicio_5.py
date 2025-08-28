'''Tendo como dados de entrada a aaltura em metros e o sexo de uma pessoa("M" masculino
 e "F" feminino), construa um programa que calcule seu peso ideal, utilizando as seguintes fórnulas:
 
 - Para homens: (72.7*h)-58
 - Para mulheres: (62.1*h)-44.7'''
 
sexo = input("Digite se você for 'M' para homem ou 'F' para mulher: ")
altura = float(input("Digite a sua altura:"))

if sexo == 'M' or 'm':
    peso = (72.7*altura)-58
elif sexo == 'F' or 'f':
    peso = (62.1)-44.7
else:
    ("Não encontrado!")
    
print(f"Seu peso ideal é: {peso:.2f}")
