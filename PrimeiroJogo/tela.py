from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase

# Define o tamanho da janela
loadPrcFileData("", "win-size 800 600")
# Define o título da janela como Minha Primeira Janela
loadPrcFileData("", "window-title Minha Primeira Janela")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        # Desativa o controle da câmera pelo mouse (ainda não usamos câmera 3D)
        self.disable_mouse()

# Inicia o programa
MyApp().run()
