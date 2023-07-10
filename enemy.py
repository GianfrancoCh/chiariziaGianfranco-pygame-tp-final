import pygame
from object import *
from auxiliar import *
from constantes import *


class Enemy(Object):
    
    ANIMATION_DELAY = 3
    COLOR = (255, 0, 0)
    GRAVITY = 1
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "enemy")
        self.enemy = load_sprite_sheets("Enemies", "Rino", width, height)
        self.image = self.enemy["Run (52x34)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.animation_count = 0
        self.animation_name = "Run (52x34)"
        self.move_direction = 1
        self.move_counter = 0
        
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 200:
            self.move_direction *= -1
            self.move_counter = 0 
        
        self.flip_sprite()  
    
    def flip_sprite(self):
        if self.move_direction == 1:
            self.image = pygame.transform.flip(self.image, True, False)
         
    def loop(self):
        sprites = self.enemy[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.update()

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            
    