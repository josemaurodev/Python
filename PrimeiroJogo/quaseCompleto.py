from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, TextNode
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import NodePath
import random

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()  # Desativa o controle padrão do mouse para a câmera

        # Inicializa o placar dos jogadores (0 a 0)
        self.score_left = 0
        self.score_right = 0
        # Cria o texto do placar na tela
        self.score_text = self.create_score_text()

        # Cria o formato dos paddles (raquetes) usando CardMaker (um retângulo)
        cm = CardMaker("q")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)  # Define as dimensões do retângulo

        # Paddle esquerdo (vermelho)
        self.q1 = self.render2d.attachNewNode(cm.generate())  # Adiciona à cena 2D
        self.q1.setColor(1, 0, 0, 1)  # Cor vermelha (RGBA)
        self.q1.setPos(-0.9, 0, 0)  # Posição fixa à esquerda da tela

        # Paddle direito (azul)
        self.q2 = self.render2d.attachNewNode(cm.generate())  # Adiciona à cena 2D
        self.q2.setColor(0, 0, 1, 1)  # Cor azul (RGBA)
        self.q2.setPos(0.9, 0, 0)  # Posição fixa à direita da tela

        # Cria a bolinha (menor que os paddles)
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)  # Define dimensões menores
        self.ball = self.render2d.attachNewNode(ball_cm.generate())  # Adiciona à cena 2D
        self.ball.setColor(1, 1, 0, 1)  # Cor amarela
        self.ball.setPos(0, 0, 0)  # Começa no centro

        # Inicializa velocidade da bola em zero para começar parada
        self.ball_dx = 0
        self.ball_dz = 0
        self.reset_ball()  # Reseta a bola e inicia o jogo

        # Adiciona tarefa para atualizar a posição da bola a cada frame
        taskMgr.add(self.atualizar_bola, "atualizar_bola")

        # Configura controles do teclado para movimentar os paddles
        self.accept("arrow_up", self.mover, [self.q1, 0, 0.05])    # Sobe paddle esquerdo
        self.accept("arrow_down", self.mover, [self.q1, 0, -0.05]) # Desce paddle esquerdo
        self.accept("w", self.mover, [self.q2, 0, 0.05])           # Sobe paddle direito
        self.accept("s", self.mover, [self.q2, 0, -0.05])          # Desce paddle direito

    def mover(self, node, dx, dz):
        # Função para mover um paddle (node) nas direções dx, dz
        x = node.getX() + dx
        z = node.getZ() + dz

        # Limita o movimento para não sair da área visível (-1 a 1)
        x = max(-1 + 0.1, min(1 - 0.1, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))

        node.setPos(x, 0, z)  # Atualiza posição do paddle

    def create_score_text(self):
        # Cria o texto que exibe o placar na tela
        self.text_node = TextNode('score')
        self.text_node.setAlign(TextNode.ACenter)  # Centraliza texto
        self.text_node.setTextColor(1, 1, 1, 1)    # Cor branca
        self.text_node.setText("0 : 0")            # Texto inicial do placar

        text_np = NodePath(self.text_node)
        text_np.reparentTo(self.aspect2d)          # Adiciona ao sistema 2D da tela
        text_np.setScale(0.1)                      # Ajusta o tamanho do texto
        text_np.setPos(0, 0, 0.9)                  # Posição no topo da tela
        return self.text_node

    def update_score(self):
        # Atualiza o texto do placar conforme os valores atuais
        self.score_text.setText(f"{self.score_left} : {self.score_right}")

    def reset_ball(self, scorer=None):
        # Reseta a posição da bola ao centro e pausa antes de lançar novamente
        # Atualiza placar se um jogador marcou
        if scorer == "left":
            self.score_left += 1
        elif scorer == "right":
            self.score_right += 1
        self.update_score()  # Atualiza visualmente o placar

        self.ball.setPos(0, 0, 0)  # Centraliza a bola
        self.ball_dx = 0            # Zera velocidade X
        self.ball_dz = 0            # Zera velocidade Z

        # Agenda o lançamento da bola após 1 segundo de pausa
        taskMgr.doMethodLater(1, self.lancar_bola, "lancar_bola")

    def lancar_bola(self, task):
        # Define uma velocidade aleatória para a bola, indo em direção aleatória
        self.ball_dx = 0.5 * random.choice([-1, 1])  # Velocidade horizontal ±0.5
        self.ball_dz = 0.5 * random.choice([-1, 1])  # Velocidade vertical ±0.5
        return Task.done  # Finaliza essa tarefa agendada

    def atualizar_bola(self, task):
        # Atualiza a posição da bola a cada frame, calculando com base no tempo delta (dt)
        dt = globalClock.getDt()
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Rebote da bola nas bordas superior e inferior (inverte velocidade vertical)
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1

        # Verifica colisão com paddle esquerdo
        if x - 0.05 <= self.q1.getX() + 0.1:
            if abs(z - self.q1.getZ()) <= 0.1:  # Checa se está na altura do paddle
                self.ball_dx *= -1  # Inverte direção horizontal da bola (rebote)
                x = self.q1.getX() + 0.1 + 0.05  # Ajusta posição para evitar "grudar"

        # Verifica colisão com paddle direito
        if x + 0.05 >= self.q2.getX() - 0.1:
            if abs(z - self.q2.getZ()) <= 0.1:  # Checa se está na altura do paddle
                self.ball_dx *= -1  # Inverte direção horizontal da bola (rebote)
                x = self.q2.getX() - 0.1 - 0.05  # Ajusta posição para evitar "grudar"

        # Se a bola sair pela esquerda → ponto para jogador da direita
        if x < -1:
            self.reset_ball(scorer="right")
            return Task.cont

        # Se a bola sair pela direita → ponto para jogador da esquerda
        if x > 1:
            self.reset_ball(scorer="left")
            return Task.cont

        # Atualiza posição da bola
        self.ball.setPos(x, 0, z)
        return Task.cont  # Continua a tarefa para o próximo frame

# Inicializa e executa o aplicativo
MyApp().run()
