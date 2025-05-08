try:
  idade = int(input("Digite a sua idade:\n"))
  print(f"Sua idade é: {idade}")
except ValueError:
  print("Valor digitado inválido")
finally:
  print("Por acaso seu nome é José?")


def jogo()
  print("Bem vindo ao jogo")
  print("Escolha com cuidados, elas importam")
  try:
    print("Voce esta na frente de tres portas. [1, 2 e 3]")
    porta = int(input("Qual porta voce quer"))

  except ValueError:
    print("Essa porta não existe")
  finally:
    print("Fim de round")

jogo()