from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, TextNode
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import NodePath
import random

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        # Placar
        self.score_left = 0
        self.score_right = 0
        self.score_text = self.create_score_text()

        cm = CardMaker("q")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)

        # Paddle esquerdo
        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)
        self.q1.setPos(-0.9, 0, 0)

        # Paddle direito
        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)
        self.q2.setPos(0.9, 0, 0)

        # Bolinha
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)
        self.ball.setPos(0, 0, 0)

        self.ball_dx = 0
        self.ball_dz = 0
        self.reset_ball()

        taskMgr.add(self.atualizar_bola, "atualizar_bola")

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

    def create_score_text(self):
        self.text_node = TextNode('score')
        self.text_node.setAlign(TextNode.ACenter)
        self.text_node.setTextColor(1, 1, 1, 1)
        self.text_node.setText("0 : 0")

        text_np = NodePath(self.text_node)
        text_np.reparentTo(self.aspect2d)
        text_np.setScale(0.1)
        text_np.setPos(0, 0, 0.9)
        return self.text_node

    def update_score(self):
        self.score_text.setText(f"{self.score_left} : {self.score_right}")

    def reset_ball(self, scorer=None):
        if scorer == "left":
            self.score_left += 1
        elif scorer == "right":
            self.score_right += 1
        self.update_score()

        self.ball.setPos(0, 0, 0)
        self.ball_dx = 0
        self.ball_dz = 0
        taskMgr.doMethodLater(1, self.lancar_bola, "lancar_bola")

    def lancar_bola(self, task):
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.5 * random.choice([-1, 1])
        return Task.done

    def atualizar_bola(self, task):
        dt = globalClock.getDt()
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Rebote nas bordas superiores/inferiores
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1

        # Colisão com paddle esquerdo
        if x - 0.05 <= self.q1.getX() + 0.1:
            if abs(z - self.q1.getZ()) <= 0.1:
                self.ball_dx *= -1
                x = self.q1.getX() + 0.1 + 0.05

        # Colisão com paddle direito
        if x + 0.05 >= self.q2.getX() - 0.1:
            if abs(z - self.q2.getZ()) <= 0.1:
                self.ball_dx *= -1
                x = self.q2.getX() - 0.1 - 0.05

        # Gol: saiu pela esquerda → ponto do jogador da direita
        if x < -1:
            self.reset_ball(scorer="right")
            return Task.cont

        # Gol: saiu pela direita → ponto do jogador da esquerda
        if x > 1:
            self.reset_ball(scorer="left")
            return Task.cont

        self.ball.setPos(x, 0, z)
        return Task.cont

MyApp().run()
