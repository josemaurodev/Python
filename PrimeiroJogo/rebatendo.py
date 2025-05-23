from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker
from panda3d.core import ClockObject
from direct.task import Task
import random

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()  
        self.disable_mouse()  # Desabilita controle de câmera padrão do Panda3D (mouse)

        cm = CardMaker("q")  # Cria um CardMaker, que gera um quadrado 2D
        cm.setFrame(-0.01, 0.01, -0.1, 0.1)  # Define tamanho do quadrado (0.2x0.2, centrado na origem)

        # Cria paddle esquerdo (vermelho) na posição x = -0.9
        self.q1 = self.render2d.attachNewNode(cm.generate())  
        self.q1.setColor(1, 0, 0, 1)  # Cor vermelha (R=1, G=0, B=0, alpha=1)
        self.q1.setPos(-0.99, 0, 0)  # Posiciona o paddle na borda esquerda da tela

        # Cria paddle direito (azul) na posição x = 0.9
        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)  # Cor azul
        self.q2.setPos(0.99, 0, 0)  # Posiciona na borda direita da tela

        # Cria a bolinha (amarela), menor que os paddles
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)  # Quadrado 0.1x0.1 para a bola
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)  # Cor amarela
        self.ball.setPos(0, 0, 0)  # Bola começa no centro

        # Define a velocidade inicial da bola em x e z, com direção aleatória (+ ou -)
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.5 * random.choice([-1, 1])

        # Adiciona a task que atualiza a posição da bola em cada frame
        self.taskMgr.add(self.atualizar_bola, "atualizar_bola")

        # Define controles para mover os paddles:
        # Paddle esquerdo (q1) controla com setas para cima e para baixo
        self.accept("w", self.mover, [self.q1, 0, 0.2])
        self.accept("s", self.mover, [self.q1, 0, -0.2])
        # Paddle direito (q2) controla com as teclas W (subir) e S (descer)
        self.accept("arrow_up", self.mover, [self.q2, 0, 0.2])
        self.accept("arrow_down", self.mover, [self.q2, 0, -0.2])

    def mover(self, node, dx, dz):
        # Move o paddle passado como parâmetro (node) nas direções dx e dz
        x = node.getX() + dx
        z = node.getZ() + dz

        # Garante que o paddle não saia da área visível (limites de -0.9 a 0.9 para x e z)
        x = max(-1 + 0.01, min(1 - 0.01, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))

        # Aplica a nova posição do paddle
        node.setPos(x, 0, z)

    def atualizar_bola(self, task):
        # Pega o tempo delta desde o último frame para movimento suave independente do FPS
        dt = globalClock.getDt()

        # Atualiza a posição da bola com base na velocidade em dx e dz
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Verifica colisão da bola com o teto e chão (limites verticais)
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1  # Inverte direção vertical para "rebater"

        # Colisão com paddle esquerdo:
        # Se a bola estiver na horizontal próxima ao paddle e a distância vertical for pequena (colisão)
        if x - 0.05 <= self.q1.getX() + 0.01:
            #z é a posição vertical da pelotinha
            #self.q2.getZ é a posição vertical do paddle q2
            #absulto disso é o calculo da distancia vertical entre o centro da bolinha e o centro do paddle
            #se a distancia por pequena, significa que bateu na raquete
            #assim, pode inverter
            if abs(z - self.q1.getZ()) <= 0.01:
                self.ball_dx *= -1  # Inverte direção horizontal para "rebater"
                x = self.q1.getX() + 0.01 + 0.05  # Ajusta posição para evitar "grudar" no paddle

        # Colisão com paddle direito:
        if x + 0.05 >= self.q2.getX() - 0.01:
            if abs(z - self.q2.getZ()) <= 0.01:
                self.ball_dx *= -1
                x = self.q2.getX() - 0.01 - 0.05

        # Atualiza a posição da bola na tela
        self.ball.setPos(x, 0, z)

        return Task.cont  # Continua executando essa task

# Cria uma instância da aplicação e executa o loop principal do Panda3D
MyApp().run()
