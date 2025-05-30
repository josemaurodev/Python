class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


#Criar dois objetos dessa classe. Com dois nomes diferentes. 
#Apresentar essas duas pessoas(objetos)

pessoa1 = Pessoa("João", 14)

pessoa1.apresentar()