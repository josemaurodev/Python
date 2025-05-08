#Pegue um valor inicial da compra do usuário
#Pegue a categoria do cliente (Comum, Vip ou Premium) usem tolower
#Caso seja Comum, não aplique desconto, caso seja vip 10%, premium 20%
#Mostre o valor final da compra
#VIP, ViP, VIp, vip, vIP, vIp

valor = 0
tipoUsuario = ""

valor = float(input("Digite o valor da sua compra:\n"))
tipoUsuario = input("Digite o seu tipo de usuário: Comum, Vip ou Premium:\n").lower()


if(tipoUsuario == "comum"):
  print("Você não ganha desconto, infelizmente. Assine nossos planos para ter desconto na compra de roupas. \n")
elif(tipoUsuario == "vip"):
  print('Você ganha 10'+ "%" +" de desconto na sua compra.")
  valor = valor - (valor*0.1)
elif(tipoUsuario == "premium"):
  print('Você ganha 20'+ "%" +" de desconto na sua compra.")
  valor = valor - (valor*0.2)
else:
  print("Categoria inválida")

print(f"O valor final da sua compra ficou: {valor}")