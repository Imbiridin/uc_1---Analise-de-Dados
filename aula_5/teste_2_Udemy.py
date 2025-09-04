'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23.'''



try:
    horario = int(input('Digite o horário de agora: '))
    
    if horario <= 11:
        print("Bom dia!")
    elif horario <= 17:
        print("Boa tarde!")
    else:
        horario <= 23
        print("Boa noite!")
except:
    print("Não encontrado!")
