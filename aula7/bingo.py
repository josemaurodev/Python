import random
import time

numeros_sorteados = set()

while len(numeros_sorteados) < 10:
  numero = random.randint(1, 50)
  if numero not in numeros_sorteados:
    numeros_sorteados.add(numero)
  print("Os numeros sorteados até agora: ", numeros_sorteados)
  time.sleep(2)

print("Tdos os numeros foram sorteados")