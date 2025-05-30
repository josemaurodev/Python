from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, TextNode
from direct.gui.DirectGui import DirectButton
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr
import random

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        self.max_score = 5
        self.score_left = 0
        self.score_right = 0
        self.jogo_ativo = True

        self.score_text = self.create_score_text()
        self.vitoria_np = None
        self.botao_reiniciar = None

        # Paddles menores para parecer paddle game
        cm = CardMaker("paddle")
        cm.setFrame(-0.02, 0.02, -0.15, 0.15)

        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)
        self.q1.setPos(-0.95, 0, 0)

        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)
        self.q2.setPos(0.95, 0, 0)

        # Bola menor
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.025, 0.025, -0.025, 0.025)
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)
        self.ball.setPos(0, 0, 0)

        self.ball_dx = 0
        self.ball_dz = 0
        self.reset_ball()

        taskMgr.add(self.atualizar_bola, "atualizar_bola")

        # Controles
        self.accept("arrow_up", self.mover, [self.q2, 0, 0.2])
        self.accept("arrow_down", self.mover, [self.q2, 0, -0.2])
        self.accept("w" or "W", self.mover, [self.q1, 0, 0.05])
        self.accept("s" or "S", self.mover, [self.q1, 0, -0.05])

    def mover(self, node, dx, dz):
        if not self.jogo_ativo:
            return
        x = node.getX() + dx
        z = node.getZ() + dz
        x = max(-1 + 0.02, min(1 - 0.02, x))
        z = max(-1 + 0.15, min(1 - 0.15, z))
        node.setPos(x, 0, z)

    def create_score_text(self):
        text_node = TextNode('score')
        text_node.setAlign(TextNode.ACenter)
        text_node.setTextColor(1, 1, 1, 1)
        text_node.setText("0 : 0")
        text_np = self.aspect2d.attachNewNode(text_node)
        text_np.setScale(0.1)
        text_np.setPos(0, 0, 0.9)
        return text_node

    def update_score(self):
        self.score_text.setText(f"{self.score_left} : {self.score_right}")

    def reset_ball(self, scorer=None):
        if not self.jogo_ativo and scorer is not None:
            return

        if scorer == "left":
            self.score_left += 1
        elif scorer == "right":
            self.score_right += 1
        self.update_score()

        # Vitória
        if self.score_left >= self.max_score:
            self.fim_de_jogo("VITÓRIA DO JOGADOR ESQUERDO!")
            return
        elif self.score_right >= self.max_score:
            self.fim_de_jogo("VITÓRIA DO JOGADOR DIREITO!")
            return

        self.ball.setPos(0, 0, 0)
        self.ball_dx = 0
        self.ball_dz = 0
        taskMgr.doMethodLater(1, self.lancar_bola, "lancar_bola")

    def fim_de_jogo(self, mensagem):
        self.jogo_ativo = False

        self.vitoria_text_node = TextNode("vitoria")
        self.vitoria_text_node.setAlign(TextNode.ACenter)
        self.vitoria_text_node.setTextColor(1, 1, 0, 1)
        self.vitoria_text_node.setText(mensagem)
        self.vitoria_np = self.aspect2d.attachNewNode(self.vitoria_text_node)
        self.vitoria_np.setScale(0.12)
        self.vitoria_np.setPos(0, 0, 0)

        # Botão reiniciar
        self.botao_reiniciar = DirectButton(
            text="Reiniciar",
            scale=0.07,
            pos=(0, 0, -0.2),
            command=self.reiniciar_jogo
        )

    def lancar_bola(self, task):
        if not self.jogo_ativo:
            return Task.done
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.5 * random.choice([-1, 1])
        return Task.done

    def atualizar_bola(self, task):
        if not self.jogo_ativo:
            return Task.cont

        dt = globalClock.getDt()
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Rebote nas bordas superior e inferior
        if z > 1 - 0.025 or z < -1 + 0.025:
            self.ball_dz *= -1

        # Colisão com paddles
        if x - 0.025 <= self.q1.getX() + 0.02:
            if abs(z - self.q1.getZ()) <= 0.15:
                self.ball_dx *= -1
                x = self.q1.getX() + 0.02 + 0.025

        if x + 0.025 >= self.q2.getX() - 0.02:
            if abs(z - self.q2.getZ()) <= 0.15:
                self.ball_dx *= -1
                x = self.q2.getX() - 0.02 - 0.025

        # Gol para a direita
        if x < -1:
            self.reset_ball(scorer="right")
            return Task.cont

        # Gol para a esquerda
        if x > 1:
            self.reset_ball(scorer="left")
            return Task.cont

        self.ball.setPos(x, 0, z)
        return Task.cont

    def reiniciar_jogo(self):
        self.score_left = 0
        self.score_right = 0
        self.update_score()

        self.q1.setPos(-0.95, 0, 0)
        self.q2.setPos(0.95, 0, 0)
        self.ball.setPos(0, 0, 0)

        self.jogo_ativo = True
        self.ball_dx = 0
        self.ball_dz = 0
        taskMgr.doMethodLater(1, self.lancar_bola, "lancar_bola")

        if self.vitoria_np:
            self.vitoria_np.removeNode()
            self.vitoria_np = None
        if self.botao_reiniciar:
            self.botao_reiniciar.destroy()
            self.botao_reiniciar = None

MyApp().run()
