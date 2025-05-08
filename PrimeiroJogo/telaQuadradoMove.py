from panda3d.core import loadPrcFileData, CardMaker, NodePath
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Quadrado Controlável")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        # Criação do quadrado
        cm = CardMaker("quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)

        self.quadrado = NodePath(cm.generate())
        self.quadrado.setColor(0, 0.5, 1, 1)  # Azul claro
        self.quadrado.setPos(0, 0, 0)
        self.quadrado.reparentTo(self.render2d)

        # Velocidade de movimento
        self.velocidade = 0.05

        # Teclas para mover
        self.accept("arrow_up", self.mover, [0, 1])
        self.accept("arrow_down", self.mover, [0, -1])
        self.accept("arrow_left", self.mover, [-1, 0])
        self.accept("arrow_right", self.mover, [1, 0])

    def mover(self, dx, dz):
        x = self.quadrado.getX()
        z = self.quadrado.getZ()
        self.quadrado.setPos(x + dx * self.velocidade, 0, z + dz * self.velocidade)

# Roda o app
MyApp().run()
