'''Uma escola solicita um programa que calcule e informa a média e a situação dos alunos. 

    Para isso o programa deverá solicitar qie o usuário informe as 4 notas.
    
    Se a média for maior ou igual a 7, deverá informar que o aluno está aprovado, senão, deverá pedir 
a nota de recuperação.
     O programa fará um novo cálculo entre a média e a nota de recuperação, caso, essa nova média 
seja inferior a 5, o programa informará que o aluno está reprovado, senão, aprovado.'''

nota1 = float(input("Digita a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno:"))
nota3 = float(input("Digite a terceira nota do aluno:"))
nota4 = float(input("Digite a quarta nota do aluno: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

if media >= 7:
    print(f"A média é {media:.2f}. Aprovado.")
else:
    print(f" A média é {media:.2f}. Recuperação.")

    recuperacao = float(input("Digite a nota de recuperação: "))
    
    final = (media + recuperacao)/2

    if final >= 5:
        print(f"Sua média final é {final:.2f}. Aprovado.")
    else: 
        print(f"Sua média final é {final:.2f}. Reprovado.")



    

    

