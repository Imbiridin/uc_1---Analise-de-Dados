'''A Martins informática comercializa os seguintes produtos:

Código  Nome       Preço
10      Pendrive   40.00
11      PowerBank  130.00
12      Headset    80.00
13      Mouse      15.00
14      Teclado    20.00

Faça um programa que fará a leitura do código e a quantidade, a cada interação, o programa
deverá perguntar se o usuário deseja continuar. Caso a resposta for 'n' , o programa exibirá a
soma e encerrará.
'''
soma = 0
total = 0

while True:
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    
    if codigo == 10:
        soma = quantidade * 40
    elif codigo == 11:
        soma = quantidade * 130
    elif codigo == 12:
        soma = quantidade * 80
    elif codigo == 13:
        soma =quantidade * 15
    else:
        codigo == 14
        soma = quantidade * 20
    
    total = total + soma
    
    continua = input("Deseja continuar s/n?: ")
    
    if continua == 's' or continua == 'S':
        continue
    elif continua == 'n' or continua == 'N':
        break
    else: 
        print("Não entedido!")
        break
    
print(f"O total a paga é R$:{total:.2f}!")