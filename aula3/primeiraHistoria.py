print("Acordei na minha cama pela manha, vi o sol nascendo.")
print("O que farei depois?")

choice1 = input("Escovarei os dentes ou tomarei banho?").lower()

if(choice1 == "escovarei os dentes"):
  print("AH, meu hálito está muito melhor.")
  choice2 = input("Irei tomar café da manhã ou jogar um lolzinho?").lower()
  if(choice2 == "tomar café"):
    print("O meu café é preto, eu gosto assim, é muito adulto.")
  elif(choice2 == "jogar um lolzinho"):
    print("Lillia é o melhor boneco do joguin, tem como não")
elif(choice1 == "tomarei banho"):
  print("Me sinto limpinho.")
