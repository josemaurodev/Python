valor = 0
tipo1 = "comum"
tipo2 = "josé"
tipo3 = "premium"

valor = float(input("Digite o valor da sua compra:\n"))
tipoUsuario = input(f"Digite o seu tipo de usuário: {tipo1}, {tipo2} ou{tipo3}:\n").lower()

if (tipoUsuario == tipo1):
  print("Você não ganha desconto, infelizmente. Assine nossos planos para ter desconto na compra de roupas. \n")

elif(tipoUsuario == tipo2):
  print('Você ganha 10'+ "%" +" de desconto na sua compra.")
  valor = valor - (valor*0.1)
elif(tipoUsuario == tipo3):
  print('Você ganha 20'+ "%" +" de desconto na sua compra.")
  valor = valor - (valor*0.2)