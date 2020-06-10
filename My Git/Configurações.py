TITULO = 'Pygame'
LARGURA = 1400
ALTURA = 700
TILE_SIZE = 70
FPS = 60
LISTA_DIFICULDADES = ['facil', 'medio', 'dificil', 'god']
DIFICULDADE = 'medio'
VIDAS = 3
PONTUACAO = 0
TEMPO_SPAWN_INIMIGO = 10000

SPRITESHEET_ENEMY = 'Enemy.png'
SPRITESHEE_KEYS = 'Keys.png'
HEART_PNG = 'Heart.png'
SPRITESHEET_HERO = 'hero_sprites.png'

#Jogador
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
GRAVIDADE = 0.8
PLAYER_JUMP = 16
VIDAS = 3

# Define estados possíveis do jogador
STILL = 0
WALKING = 1
JUMPING = 2
FIGHTING = 3
SWIMMING = 4
FALLING = 2

#MAPA TILES
CHAO = 1
TERRA = 2
CEU = 3
BASE = 4

MAP = [
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	BASE,	BASE,	BASE,	BASE,	BASE,	BASE,	BASE,   BASE,   BASE,   BASE],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [BASE,	BASE,	BASE,	BASE,	BASE,	BASE,	BASE,	BASE,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU,	CEU],
    [CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO,	CHAO],
    [TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA,	TERRA],
  
]


#Tela
TITLE = 'Bem vindo'
FONT_NAME = 'Courier'

#Cores para ser utilizada
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (106, 159, 181)
YELLOW = (255, 255, 0)
GREEN2 = (102,255,178)