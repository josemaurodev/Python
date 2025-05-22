from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker
from panda3d.core import ClockObject
from direct.task import Task
import random

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("q")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)

        # Paddle esquerdo (vermelho)
        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)
        self.q1.setPos(-0.9, 0, 0)

        # Paddle direito (azul)
        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)
        self.q2.setPos(0.9, 0, 0)

        # Bolinha (amarela)
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)
        self.ball.setPos(0, 0, 0)

        # Direção inicial aleatória
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.5 * random.choice([-1, 1])

        self.taskMgr.add(self.atualizar_bola, "atualizar_bola")

        # Controles
        self.accept("arrow_up", self.mover, [self.q1, 0, 0.05])
        self.accept("arrow_down", self.mover, [self.q1, 0, -0.05])
        self.accept("w", self.mover, [self.q2, 0, 0.05])
        self.accept("s", self.mover, [self.q2, 0, -0.05])

    def mover(self, node, dx, dz):
        x = node.getX() + dx
        z = node.getZ() + dz
        x = max(-1 + 0.1, min(1 - 0.1, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))
        node.setPos(x, 0, z)

    def atualizar_bola(self, task):
        dt = globalClock.getDt()
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Rebote vertical (teto e chão)
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1

        # Colisão com paddle esquerdo
        if x - 0.05 <= self.q1.getX() + 0.1:
            if abs(z - self.q1.getZ()) <= 0.1:
                self.ball_dx *= -1
                x = self.q1.getX() + 0.1 + 0.05  # Evita prender

        # Colisão com paddle direito
        if x + 0.05 >= self.q2.getX() - 0.1:
            if abs(z - self.q2.getZ()) <= 0.1:
                self.ball_dx *= -1
                x = self.q2.getX() - 0.1 - 0.05  # Evita prender

        self.ball.setPos(x, 0, z)
        return Task.cont

MyApp().run()
