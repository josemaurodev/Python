#pegar uma frase
#frase = input("Digite uma frase:\n").lower()
#percorrer uma frase
#for ou while

#pegar uma variavel inteira e mostrar os numeros de 0 a 10

num = 0
for num in range(10):
  print(f"{num}")

nomes = ["Gustavo", "José", "Thales", "Limite", "Quantos", "Quiser"]
# for nomes in range(3):
#   print(f"O nomes são: {nomes}")

for nome in nomes:
  print(nome)

numero = int(input("Digite um numero: 1 a 10 - 3 tentativas"))
sorte = 0

while sorte != 3 :
  if(numero == 3):
    print ("Você acertou")
  elif(numero != 3):
    print ("Você errou")
    sorte = sorte + 1
  