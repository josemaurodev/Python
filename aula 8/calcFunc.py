#pegar dois valores do usuario
#pegar a operacao do usuario
#conforme a operacao chamar uma funcao
#mostrar o resultado final

import time
def subtraçãoOrdem(a, b, sequencia):
  match(sequencia):
    case 1:
      print("Calculando...")
      time.sleep(3)
      resultadof = a - b
    case 2:
      print("Calculando...")
      time.sleep(3)
      resultadof = b - a
  return resultadof

def somaOrdem(i, j, order):
  match(order):
    case 1:
      print("Calculando...")
      time.sleep(3)
      resultado = i + j
    case 2:
      print("Calculando...")
      time.sleep(3)
      resultado = j + i
  return resultado
def subtração(c, d):
  print("Digite a ordem:\n1 - Primeiro + Segundo\n2 - Segundo + Primeiro")
  sequencia = int(input())
  return subtraçãoOrdem(c, d, sequencia)

def soma(x, y):
  print("Digite a ordem:\n1 - Primeiro + Segundo\n2 - Segundo + Primeiro")
  ordem = int(input())
  return somaOrdem(x, y, ordem)

print("Bem vindo a calculadora\n")
print("Digite qual operação você deseja realizar:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão")
operacao = int(input())
print("Digite qual o primeiro numero:\n")
valor1 = int(input())
print("Digite qual o segundo numero:\n")
valor2 = int(input())
if operacao == 2:
  resultadoFinal = subtração(valor1, valor2)
print(f"O resultado final é: {resultadoFinal}")
resultadoFinal = soma(valor1, valor2)
print(f"O resultado final é: {resultadoFinal}")
