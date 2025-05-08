numero = input("Digite um número: ")

if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
    numero = int(numero)
    
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("Erro: O valor digitado não é um número inteiro.")
