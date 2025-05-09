#da panda importa a tela
from panda3d.core import loadPrcFileData
#da panda, importa a capacidade de mostrar a tela
from direct.showbase.ShowBase import ShowBase

# Define o tamanho da janela
loadPrcFileData("", "win-size 1260 780")
# Define o título da janela como Minha Primeira Janela Modificada
loadPrcFileData("", "window-title Minha Primeira Janela")

class MyApp(ShowBase):
    def __init__(self):
        # Chama o construtor da classa ShowBase
        super().__init__()
        # Desativa o controle da câmera pelo mouse (ainda não usamos câmera 3D)
        self.disable_mouse()

# Inicia o programa
MyApp().run()
