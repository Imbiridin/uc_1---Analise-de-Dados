
numero1 = int(input("Digite o primeiro número para ser somado:"))
operador = input("Digite o operador desejável entre: (+, -, *,/):")
numero2 = int(input("Digite o segundo número para ser somado:"))

while True:
  
  if operador == "+":
      soma = numero1+numero2
      print(f"{numero1}+{numero2}={soma}")
  elif operador == "-":
      soma = numero1-numero2
      print(f'{numero1}-{numero2}={soma}')
  elif operador == "*":
      soma = numero1*numero2
      print(f'{numero1}*{numero2}={soma}')
  elif operador == "/":
      soma = numero1/numero2
      print(f'{numero1}/{numero2}={soma}')
  else:
      print("Não encontrado")
  break
