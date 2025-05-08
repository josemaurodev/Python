#pegar uma frase e salvar em uma variavel
frase = input("Digite aqui uma frase:\n").lower()
#declarar uma variavel para contar as vogais
contaVogais = 0
#percorrer a frase
for vogal in frase:
#  se a palavraLetra.lower() tiver aeiou
  if vogal.lower() in 'aeiou':
#  somar +1 na variavel que conta
    contaVogais = contaVogais+1
#mostra o seguinte: a frase x tem x vogais
print(f"A frase '{frase}' tem {contaVogais}.")