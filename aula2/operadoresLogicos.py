#calculadora dois numeros

numero1 = 0
numero2 = 0
operacao = ""
resultado = 0

numero1 = float(input("Digite o primeiro numero:\n"))
numero2 = float(input("Digite o segundo numero:\n"))
operacao = input("Digite a operacao (+, -, /, *, <,>, op3):\n")

if(operacao == "+"): #operador logico de igualdade
  resultado = numero1 + numero2
  print(f"O resultado é: {resultado}")
elif(operacao == "-"): #operador logico de igualdade
  resultado = numero1 - numero2
  print(f"O resultado é: {resultado}") 
elif(operacao == "/"): #operador logico de igualdade
  resultado = numero1 / numero2
  print(f"O resultado é: {resultado}")
elif(operacao == "*"): #operador logico de igualdade
  resultado = numero1 * numero2
  print(f"O resultado é: {resultado}")
elif(operacao == "<"):
  #comparar os numeros
  if(numero1 < numero2): #operador logico de comparacao
  #mostrar que "O numero 1 é menor que o numero 2" OU
    print(f"{numero1} é menor que {numero2}")
  #mostrar que "O numero 2 é menor que o numero 1"
  elif(numero2 < numero1): #operador logico de comparacao
    print(f"{numero2} é menor que {numero1}")
  else:
    print(f"Os dois numeros são iguais")
elif(operacao == ">"):
  #comparar os numeros
  if(numero1 > numero2): #operador logico de comparacao
  #mostrar que "O numero 1 é menor que o numero 2" OU
    print(f"{numero2} é menor que {numero1}")
  #mostrar que "O numero 2 é menor que o numero 1"
  elif(numero1 < numero2): #operador logico de comparacao
    print(f"{numero1} é menor que {numero2}")
  else:
    print(f"Os dois numeros são iguais")
if(operacao == "op3"):
  numero3 = 0
  numero3 = float(input("Digite o terceiro numero:\n"))
  if((numero1 > numero2) and (numero1 > numero3) and (numero2 > numero3)):
    print(f"O {numero1} é o maior número, o {numero2} é o do meio e o {numero3} é o menor")
  elif((numero1 > numero2) and (numero1 < numero3)):
    print(f"O {numero1} é o maior número, o {numero2} é o do meio e o {numero3} é o menor")
  




#termina aqui