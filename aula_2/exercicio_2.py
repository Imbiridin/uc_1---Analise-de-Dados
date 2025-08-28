import datetime

anoN = int(input("Digite o ano que você nasceu:"))
#anoA = int(input("Digite o ano atual:"))

anoatual = datetime.datetime.now().year
mesatual = datetime.datetime.now().month
diaatual = datetime.datetime.now().day

idadeA = anoatual - anoN
idadeM = mesatual * 12
idadeD = diaatual * 365

print(f"\nSua idade é {idadeA}.\nSua idade em meses é: {idadeM}.\nSua idade em dias é: {idadeD}.")