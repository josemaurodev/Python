nota1 = 0
nota2 = 0
nota3 = 0

nota1 = float(input("Digite a nota 1\n"))
nota2 = float(input("Digite a nota 2\n"))
nota3 = float(input("Digite a nota 3\n"))

media = (nota1+nota2+nota3)/3

if(media>7):
  print("Aprovado")
elif(media<5):
  print("Reprovado")
elif(media<=7 and media >=5):
  print("Recuperação")