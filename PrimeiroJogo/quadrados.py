from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("q1")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)
        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)
        self.q1.setPos(-0.5, 0, 0)

        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)
        self.q2.setPos(0.5, 0, 0)

        # Controles do quadrado 1 (setas)
        self.accept("arrow_up", self.mover, [self.q1, 0, 0.05])
        self.accept("arrow_down", self.mover, [self.q1, 0, -0.05])
        self.accept("arrow_left", self.mover, [self.q1, -0.05, 0])
        self.accept("arrow_right", self.mover, [self.q1, 0.05, 0])

        # Controles do quadrado 2 (WASD)
        self.accept("w" or "W", self.mover, [self.q2, 0, 0.05])
        self.accept("s" or "S", self.mover, [self.q2, 0, -0.05])
        self.accept("a" or "A", self.mover, [self.q2, -0.05, 0])
        self.accept("d" or "D", self.mover, [self.q2, 0.05, 0])

    def mover(self, node, dx, dz):
        x = node.getX() + dx
        z = node.getZ() + dz
        x = max(-1 + 0.1, min(1 - 0.1, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))
        node.setPos(x, 0, z)

MyApp().run()
