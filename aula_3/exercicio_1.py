'''Elabore um programa que dada a idade de um nadador classifica-o em uma das seguintes categorias:


infantil A = 5 - 7 anos
infantil B = 8 - 10 anos
juvenil A = 11 - 13 anos
juvenil B = 14 - 17 anos
adulto = maiores de 18 anos

'''

nadadorI = int(input("Digite a sua idade: "))


if nadadorI <= 4:
    print("Você é muito novo!")
elif nadadorI == 5 or nadadorI <= 7:
    print("infatil A")
elif nadadorI == 8 or nadadorI <= 10:
    print("infantil B")
elif nadadorI == 11 or nadadorI <= 13:
    print("juvenil A")
elif nadadorI == 14 or nadadorI <= 17:
    print("juvenil B")
else: print("adulto")

    