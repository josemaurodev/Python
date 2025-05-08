#declar uma variavel e pegar o numero de passos que a pessoa quer dar no dia
meta = int(input("Digite a meta de passos:\n"))
#declarar uma variavel para contar os passos
contPassos = 0
#Enquanto a variavel de contagem for menor que a o objetivo
while contPassos < meta:
  #mostra para a pessoa quantos passos ela deu e quantos ela precisa para atingir o goal
  print(f"Você deu até o momento {contPassos}.")
  #peça para a pessoa digitar quantos passos ela deu agora
  passosTotais = int(input("Você ainda não terminou sua meta. Quantos passou você deu agora?\n"))
  #soma pacos até o momento com os passos que ela digitou que deu
  contPassos = passosTotais + contPassos

#mostra uma mensagem de parabens
print("Você atingiu sua meta! Parabéns!")