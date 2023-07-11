import pygame
from pygame import font


WIDTH, HEIGHT = 1248, 768
# WIDTH, HEIGHT = 1100, 672
FPS = 60
PLAYER_VEL = 5
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
MENU_FONT = pygame.font.SysFont("arialblack", 40)

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0 , 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 160)
PEACH = (255, 118, 95)
BLUE_2 = (38, 0, 160)
YELLOW_2 = (255, 174, 0)
GREEEN_2 = (38, 137, 0)
ORANGE = (255, 81, 0)

# MOUSE CONSTANTS
M_STATE_NORMAL = 0
M_STATE_HOVER = 1
M_STATE_CLICK = 3
M_BRIGHT_HOVER = (32,32,32)
M_BRIGHT_CLICK = (32,32,32)




SONIDO_FRUTA = pygame.mixer.Sound('sound/collected.mp3')
SONIDO_BG = pygame.mixer.Sound('sound/bg.mp3')
SONIDO_DAÑO = pygame.mixer.Sound('sound/hit1.wav')
HEART = pygame.image.load("assets/Other/heart pixel 32x32.png")
HEART_LOST = pygame.image.load("assets/Other/heart_white 12x12.png")
WINDOW  = pygame.display.set_mode((WIDTH, HEIGHT))      
# DISSAPEAR = pygame.image.load()