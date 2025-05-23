from direct.showbase.ShowBase import ShowBase        # Importa a classe base do Panda3D para criar a aplicação
from panda3d.core import CardMaker, ClockObject                  # Importa para criar formas geométricas simples (cards)  # Importa para controle do tempo (delta time)
from direct.task import Task                           # Importa para criar tarefas que rodam a cada frame
import random                                         # Importa para gerar números aleatórios

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()                            # Inicializa a aplicação base do Panda3D
        self.disable_mouse()                          # Desativa o controle padrão do mouse para a câmera

        # Cria um "card" (um quadrado 2D) para os jogadores
        cm = CardMaker("q")
        cm.setFrame(-0.01, 0.01, -0.1, 0.1)            # Define o tamanho do card (0.2x0.2 unidades)

        # Cria o jogador 1 (quadrado vermelho) e posiciona na esquerda da tela
        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)                  # Cor vermelha (RGBA)
        self.q1.setPos(-0.99, 0, 0)                    # Posição no eixo x: -0.9 (esquerda)

        # Cria o jogador 2 (quadrado azul) e posiciona na direita da tela
        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)                  # Cor azul
        self.q2.setPos(0.99, 0, 0)                     # Posição no eixo x: 0.9 (direita)

        # Cria a bolinha (quadrado amarelo menor)
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)    # Menor que os jogadores (0.1x0.1 unidades)
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)                # Cor amarela
        self.ball.setPos(0, 0, 0)                      # Começa no centro da tela

        # Define a velocidade da bolinha em x e z com direções aleatórias
        # 0.5 é a velocidade, multiplicada por -1 ou 1 para indicar direção
        # Adiciona a tarefa que atualiza a posição da bolinha a cada frame
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.6 * random.choice([-1, 1])
        self.taskMgr.add(self.atualizar_bola, "atualizar_bola")


        # Define os controles dos jogadores (teclas para mover para cima e para baixo)
        self.accept("w" or "W", self.mover, [self.q1, 0, 0.05])    # Jogador 1 sobe (seta para cima)
        self.accept("s" or "S", self.mover, [self.q1, 0, -0.05]) # Jogador 1 desce (seta para baixo)
        self.accept("arrow_up", self.mover, [self.q2, 0, 0.05])           # Jogador 2 sobe (tecla W)
        self.accept("arrow_down", self.mover, [self.q2, 0, -0.05])          # Jogador 2 desce (tecla S)

    # Função para mover um objeto (node) somando dx e dz à sua posição atual,
    # garantindo que ele fique dentro dos limites da tela (-1 a 1 menos margem)
    def mover(self, node, dx, dz):
        x = node.getX() + dx
        z = node.getZ() + dz
        # Limita posição para não sair da tela (com margem 0.1)
        x = max(-1 + 0.01, min(1 - 0.01, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))
        node.setPos(x, 0, z)

    # Tarefa chamada a cada frame para atualizar a posição da bolinha
    def atualizar_bola(self, task):
        dt = globalClock.getDt()                         # Obtém o tempo delta (tempo desde o último frame)
        x = self.ball.getX() + self.ball_dx * dt        # Atualiza posição x da bola com base na velocidade
        z = self.ball.getZ() + self.ball_dz * dt        # Atualiza posição z da bola

        # Verifica colisão com as bordas superior e inferior (rebote invertendo direção em z)
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1

        # Verifica colisão com as bordas laterais (rebote invertendo direção em x)
        # No futuro, essas colisões podem ser substituídas por pontuação
        if x > 1 - 0.05 or x < -1 + 0.05:
            self.ball_dx *= -1

        self.ball.setPos(x, 0, z)                        # Aplica a nova posição da bola
        return Task.cont                                 # Continua a tarefa no próximo frame

# Executa o jogo
MyApp().run()
