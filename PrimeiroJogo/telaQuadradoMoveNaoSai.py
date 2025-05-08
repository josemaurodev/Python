from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)
        self.quadrado = self.render2d.attachNewNode(cm.generate())
        self.quadrado.setColor(0.5, 1, 0.5, 1)

        self.accept("arrow_up", self.mover, [0, 0.05])
        self.accept("arrow_down", self.mover, [0, -0.05])
        self.accept("arrow_left", self.mover, [-0.05, 0])
        self.accept("arrow_right", self.mover, [0.05, 0])

    def mover(self, dx, dz):
        x = self.quadrado.getX() + dx
        z = self.quadrado.getZ() + dz
        x = max(-1 + 0.1, min(1 - 0.1, x))  # Clamp horizontal
        z = max(-1 + 0.1, min(1 - 0.1, z))  # Clamp vertical
        self.quadrado.setPos(x, 0, z)

MyApp().run()
