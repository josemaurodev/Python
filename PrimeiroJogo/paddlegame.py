# Importa algumas ferramentas necessárias do Panda3D
from panda3d.core import loadPrcFileData, WindowProperties
from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath, CardMaker
from direct.task import Task
import random  # Biblioteca para gerar números aleatórios

# Define o título da janela e seu tamanho (largura e altura)
define_window_title = "Paddle Game"
define_window_width = 1280
define_window_height = 720

# Define o tamanho da janela com os valores acima
loadPrcFileData("", f"win-size {define_window_width} {define_window_height}")
# Faz com que a janela não possa ser redimensionada
loadPrcFileData("", "win-fixed-size #t")
# Coloca um nome na janela
loadPrcFileData("", f"window-title {define_window_title}")

# Cria a classe principal do jogo
class PaddleGame(ShowBase):

  def __init__(self):
    # Inicia o Panda3D
    super().__init__()

    # Configura a janela
    self.set_window_properties()

    # Desliga o controle da câmera com o mouse (não vamos usar a câmera aqui)
    self.disable_mouse()

    # Define a velocidade da bola
    self.ball_speed = 0.01

    # Define uma direção inicial aleatória para a bola
    self.ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Velocidade dos paddles (as "raquetes")
    self.paddle_speed = 0.2

    # Cria a bola vermelha no centro da tela
    self.ball = self.create_square(0, 0 , 0.05, color = (1, 0, 0 , 1))

    # Define largura e altura das raquetes
    paddle_width = 0.02
    paddle_height = 0.2

    # Cria a raquete esquerda (verde)
    self.paddle_left = self.create_rectangle(-1 + paddle_width, 0, paddle_width, paddle_height, color=(0, 1, 0, 1))
    # Cria a raquete direita (azul)
    self.paddle_right = self.create_rectangle(1 - paddle_width, 0, paddle_width, paddle_height, color=(0, 0, 1, 1))

    # Define as teclas de controle das raquetes
    self.accept("w", self.move_paddle, [self.paddle_left, 1])       # W sobe a raquete esquerda
    self.accept("s", self.move_paddle, [self.paddle_left, -1])      # S desce a raquete esquerda
    self.accept("arrow_up", self.move_paddle, [self.paddle_right, 1])    # Seta para cima sobe a raquete direita
    self.accept("arrow_down", self.move_paddle, [self.paddle_right, -1]) # Seta para baixo desce a raquete direita

    # Cria uma tarefa que será executada a cada frame (atualização da tela)
    self.task_mgr.add(self.update_game, "updateGame")

  # Configura o tamanho da janela e bloqueia o redimensionamento
  def set_window_properties(self):
    props = WindowProperties()
    props.setSize(define_window_width, define_window_height)
    props.setFixedSize(True)
    self.win.requestProperties(props)

  # Cria um quadrado na tela (usado para a bola)
  def create_square(self, x, y, size, color = (1,1,1,1)):
    cm = CardMaker("square")  # Cria o formato
    cm.setFrame(-size/2, size/2, -size/2, size/2)  # Define os limites do quadrado
    square = NodePath(cm.generate())  # Gera o objeto no Panda3D
    square.setPos(x, 0, y)  # Define a posição do quadrado na tela (x e y invertido com z)
    square.setColor(*color)  # Define a cor do quadrado
    square.reparentTo(self.render2d)  # Adiciona à tela 2D
    return square  # Retorna o objeto criado

  # Cria um retângulo (usado para as raquetes)
  def create_rectangle(self, x, y, width, height, color = (1,1,1,1)):
    cm = CardMaker("rectangle")  # Cria o formato
    cm.setFrame(-width/2, width/2, -height/2, height/2)  # Define os limites do retângulo
    square = NodePath(cm.generate())  # Gera o objeto no Panda3D
    square.setPos(x, 0, y)  # Define a posição na tela
    square.setColor(*color)  # Define a cor
    square.reparentTo(self.render2d)  # Adiciona à tela 2D
    return square  # Retorna o objeto

  # Move a raquete para cima ou para baixo
  def move_paddle(self, paddle, direction):
    paddle_height = 0.2  # Altura da raquete
    new_y = paddle.getZ() + direction * self.paddle_speed  # Calcula nova posição
    uper_limit = 1 - (paddle_height / 2)  # Limite superior
    lower_limit = -1 + (paddle_height / 2)  # Limite inferior
    # Só move se estiver dentro dos limites
    if lower_limit <= new_y <= uper_limit:
      paddle.setZ(new_y)  # Atualiza a posição da raquete

  # Atualiza o jogo a cada frame
  def update_game(self, task):
    # Pega a posição atual da bola
    ball_pos = self.ball.getPos()
    # Calcula a nova posição da bola
    new_x = ball_pos.x + self.ball_direction[0] * self.ball_speed
    new_y = ball_pos.z + self.ball_direction[1] * self.ball_speed

    # Verifica se a bola bateu no topo ou embaixo da tela
    if new_y > 1 or new_y < -1:
      self.ball_direction[1] *= -1  # Inverte a direção vertical da bola

    # Verifica colisão com as raquetes
    if (new_x < -1 + 0.04 and abs(self.paddle_left.getZ() - new_y) < 0.2) or \
       (new_x > 1 - 0.04 and abs(self.paddle_right.getZ() - new_y) < 0.2):
      self.ball_direction[0] *= -1  # Inverte a direção horizontal da bola

    # Verifica se a bola saiu da tela (ponto para alguém)
    if new_x < -1.2 or new_x > 1.2:
      self.ball.setPos(0, 0, 0)  # Reinicia a bola no meio
      self.ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]  # Direção aleatória
      return Task.cont  # Continua o jogo

    # Move a bola para a nova posição
    self.ball.setPos(new_x, 0 , new_y)
    return Task.cont  # Continua atualizando

# Inicia o jogo
if __name__ == "__main__":
  PaddleGame().run()
