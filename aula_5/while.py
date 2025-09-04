#Ler indeterminados números inteiros e informar a soma

soma = 0

while True:
    n = int(input("Informe o número: "))
    soma = soma + n
    print(f"A soma é {soma}")
    
    r = input("Deseja continuar s/n ?: ")
    if r == 's' or r == 'S':
     continue
    elif r == 'n' or r == 'N':
        break
    else:
        print("Não entendido!")
        break
