def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2

def menu():
    print("Escolha a operação:")
    print("+ ou soma")
    print("- ou sub")
    print("* ou mul")
    print("/ ou div")
    
    op = input("Operação: ")
    var1 = float(input("Digite o primeiro número: "))
    var2 = float(input("Digite o segundo número: "))

    if op == "+" or op == "soma":
        res = soma(var1, var2)
        print(f"O resultado da soma é {res}")
    elif op == "-" or op == "sub":
        res = sub(var1, var2)
        print(f"O resultado da subtração é {res}")
    elif op == "*" or op == "mul":
        res = mul(var1, var2)
        print(f"O resultado da multiplicação é {res}")
    elif op == "/" or op == "div":
        res = div(var1, var2)
        print(f"O resultado da divisão é {res}")
    else:
        print("Operação inválida.")

menu()