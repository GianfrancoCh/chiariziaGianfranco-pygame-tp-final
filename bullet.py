import pygame
from object import *
from auxiliar import *
from constantes import *


class Bullet(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    SPEED = 1

    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("assets/Other/bullet.png")
        # self.image.fill(self.COLOR)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        if self.direction == "right":
            self.rect.x += self.SPEED
        elif self.direction == "left":
            self.rect.x -= self.SPEED

        if self.rect.x > WIDTH or self.rect.x < 0:  # Eliminar la bala cuando salga de la ventana
            self.kill()
    
    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        