#Fazer um banco onde o usuario cria um cadastro. 
#Faz um saque. 
#E faz um deposito.
#Dicionario, nome, idade e saldo.
#Se tiver que menos que 18, não pode.
#Se tiver mais que 1000R$, arrendondar para 1000R$.
#Usar funcoes
#Usar funcoes diferentes para cada proposito. 
#As funcoes que puderem ter retorno, devem ter retorno.
#TEMAS: ADICIONAR DICIONARIO DE CONTAS

def criar_conta():
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))

  if idade < 18:
    print("Cadastro não permitido. Você precisa ter 18 anos ou mais.")
    return None

  saldo = float(input("Digite o saldo inicial: "))
  if saldo > 1000:
    print("Saldo inicial muito alto. Será ajustado para R$1000.")
    saldo = 1000.0

  conta = {"nome": nome, "idade": idade, "saldo": saldo}
  print(f"Conta criada para {nome} com saldo de R${saldo:.2f}")
  return conta

def depositar():
def sacar():

def banco():
  conta = criar_conta()
  if conta is None:
      return
  while True:
    print("\n -- Menu Principal Banco Happy --")
    print("1 - Ver saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: \n"))
banco()