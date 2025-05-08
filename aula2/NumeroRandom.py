import random

numeroRandomico = random.randint(1,10)
guessed = False
tentativa = 0

print("Bem vindo ao jogo de advinhação:")
while not guessed:
  guess = int(input("Digite um numero\n"))
  tentativa = tentativa+1
  #tentativa += 1
  if(guess<numeroRandomico):
    print("Numero mais baixo que o randomico, tente de novo")
  elif(guess>numeroRandomico):
    print("Numero mais alto que o randomico, tente de novo")
  else:
    guessed = True
    print(f"Parabens, você acertou o numero, o numero era {numeroRandomico}")
    #print(f"O numero era {numeroRandomico}, parabens, você acertou")
    #print("O numero era", numeroRandomico, "parabens você acertou")
    #print("Parabens, você acertou o numero, o numero era ", numeroRandomico)
    print(f"Voce demorou {tentativa}")
  