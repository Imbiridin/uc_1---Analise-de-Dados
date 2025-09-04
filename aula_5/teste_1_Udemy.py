'''Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.'''

try:
    numero = int(input("Digite um número para saber se é par ou ímpar: "))
    if numero % 2 == 0:
        print("Seu número é par!")
    else:
        print("Seu número é ímpar!")
except:
    print("Seu número não é inteiro!")
