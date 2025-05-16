from panda3d.core import loadPrcFileData, CardMaker
from panda3d.core import WindowProperties, NodePath
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Quadrado na Tela")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        # Cria o quadrado (com o CardMaker)
        cm = CardMaker("meu_quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)  # Largura e altura do quadrado

        # Cria a geometria e embrulha ela no nó
        quadrado = NodePath(cm.generate())
        # Muda as características desse nó
        quadrado.setColor(1, 0, 1, 1)  # Cor vermelha (R, G, B, A)
        quadrado.setPos(0, 0, 0)       # Posição central (x, y, z)
        quadrado.reparentTo(self.render2d)  # Adiciona o quadrado na tela 2D

# Roda o app
MyApp().run()
