import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
import time
from player import *
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1200, 768
# WIDTH, HEIGHT = 1100, 672
FPS = 60
PLAYER_VEL = 5
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
BLACK = (0, 0, 0)

SONIDO_FRUTA = pygame.mixer.Sound('sound/collected.mp3')
SONIDO_BG = pygame.mixer.Sound('sound/bg.mp3')
SONIDO_DAÑO = pygame.mixer.Sound('sound/hit1.wav')
HEART = pygame.image.load("assets/Other/heart pixel 32x32.png")
HEART_LOST = pygame.image.load("assets/Other/heart_white 12x12.png")
# DISSAPEAR = pygame.image.load()

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_flag(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(288, 144, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

# def heart(size):
#     path = join("Other", "Terrain", "Terrain.png")
#     image = pygame.image.load(path).convert_alpha()
#     surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
#     rect = pygame.Rect(288, 144, size, size)
#     surface.blit(image, (0, 0), rect)
#     return pygame.transform.scale2x(surface)

# class Player(pygame.sprite.Sprite):
#     COLOR = (255, 0, 0)
#     GRAVITY = 1
#     SPRITES = load_sprite_sheets("MainCharacters", "PinkMan", 32, 32, True)
   
#     ANIMATION_DELAY = 3

#     def __init__(self, x, y, width, height):
#         super().__init__()
        
#         self.rect = pygame.Rect(x, y, width, height)
#         self.x_vel = 0
#         self.y_vel = 0
#         self.mask = None
#         self.direction = "left"
#         self.animation_count = 0
#         self.fall_count = 0
#         self.jump_count = 0
#         self.hit = False
#         self.hit_count = 0
#         self.hit_time = 0
#         self.hit_delay = 3
#         self.score = 0
#         self.shoot = False
#         self.shoot_count = 0
#         self.last_shot_time = 0
#         self.shoot_delay = 0.5 
#         self.bullets = pygame.sprite.Group()
#         self.lives = 3
#         self.flag_got_points = False
#         self.points = 0
#         self.last_point_time = 0
#         self.point_delay = 0.5
        


#     def manage_lives(self):
        
#         if self.lives > 0:
#             lives = self.lives
#             for l in range(lives):
#                 window.blit(HEART, (100 + (l*34),8))
#         else:
#             print("MUERTO")
        
#     def manage_points(self):  
            
#         current_time = time.time()
#         if not self.flag_got_points or (current_time - self.last_point_time) >= self.point_delay:
#             self.flag_got_points = True
#             self.hit_time = current_time
#             self.points += 10
        
        
#     def jump(self):
#         self.y_vel = -self.GRAVITY * 8
#         self.animation_count = 0
#         self.jump_count += 1
#         if self.jump_count == 1:
#             self.fall_count = 0

#     def move(self, dx, dy):
#         self.rect.x += dx
#         self.rect.y += dy

#     def make_hit(self):
        
#         current_time = time.time()
#         if not self.hit or (current_time - self.hit_time) >= self.hit_delay:
#             self.hit = True
#             self.hit_time = current_time
#             self.lives -= 1
#             SONIDO_DAÑO.play()
#             self.update_sprite()
        
#     def make_shoot(self):
#         current_time = time.time()
#         if current_time - self.last_shot_time >= self.shoot_delay:
#             self.last_shot_time = current_time
#             self.shoot = True
#             bullet = Bullet(self.rect.x, self.rect.y + self.rect.height // 2, self.direction) 
#             self.bullets.add(bullet) 

#     def move_left(self, vel):
#         self.x_vel = -vel
#         if self.direction != "left":
#             self.direction = "left"
#             self.animation_count = 0

#     def move_right(self, vel):
#         self.x_vel = vel
#         if self.direction != "right":
#             self.direction = "right"
#             self.animation_count = 0

#     def loop(self, fps):
#         self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
#         self.move(self.x_vel, self.y_vel)

#         if self.hit:
#             self.hit_count += 1
#         if self.hit_count > fps * 3:
#             self.hit = False
#             self.hit_count = 0
            
#         if self.shoot:
#             self.shoot_count += 1
#         if self.shoot_count > fps/3:
#             self.shoot = False
#             self.shoot_count = 0

#         self.fall_count += 1
        
#         self.update_sprite()

#     def landed(self):
#         self.fall_count = 0
#         self.y_vel = 0
#         self.jump_count = 0

#     def hit_head(self):
#         self.count = 0
#         self.y_vel *= -1

        
#     def update_sprite(self):
#         sprite_sheet = "idle"
#         if self.hit:
#             sprite_sheet = "hit"
#             # SONIDO_DAÑO.play()
#         elif self.shoot:
#             sprite_sheet = "test"
#         elif self.y_vel < 0:
#             if self.jump_count == 1:
#                 sprite_sheet = "jump"
#             elif self.jump_count == 2:
#                 sprite_sheet = "double_jump"
#         elif self.y_vel > self.GRAVITY * 2:
#             sprite_sheet = "fall"
#         elif self.x_vel != 0:
#             sprite_sheet = "run"
        
        
#         sprite_sheet_name = sprite_sheet + "_" + self.direction
#         sprites = self.SPRITES[sprite_sheet_name]
#         sprite_index = (self.animation_count //
#                         self.ANIMATION_DELAY) % len(sprites)
#         self.sprite = sprites[sprite_index]
#         self.animation_count += 1
#         self.update()

        
#     def update(self):
#         self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
#         self.mask = pygame.mask.from_surface(self.sprite)
        
#         self.bullets.update()

#     def draw(self, win, offset_x):
#         win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
#         self.manage_lives()
        
#         # draw_text(str(self.points),300, 8)


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
    

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
        
                  
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "block")
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
    
        
class Flag(Object):
     def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "flag")
        block = get_flag(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image) 
    
class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            
            
class Fruit(Object):
    
    ANIMATION_DELAY = 3
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fruit")
        self.fruit = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.fruit["Apple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Apple"
        self.should_disappear = False
        
    def loop(self):
        sprites = self.fruit[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
       
    def update(self):
        if pygame.sprite.collide_mask(self, Player):
            self.kill()
            
    
            
  
    # def collision_check(self, player_rect):
    #     if self.rect.colliderect(player_rect):
    #         self.should_disappear = True
        
        

def get_background(name):
    image = pygame.image.load(join("assets/Background", name))

    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x):
    
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)
    
    for bullet in player.bullets:
        bullet.draw(window, offset_x)
            
    # draw_winner(str(player.score))
   
    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break
      

    player.move(-dx, 0)
    player.update()
    return collided_object


def draw_text(text, x, y):
    
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    window.blit(draw_text, (x,y))
    pygame.display.update()
   
    
    
    

def handle_move(player, objects):
    
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)
    
    
    if keys[pygame.K_a] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check_vertical = [*vertical_collide]
    to_check_sides = [collide_left, collide_right]

            
    for obj in to_check_sides:
        if obj and obj.name == "fire":
            player.make_hit()
            # draw_winner("FUEGO")
        if obj and obj.name == "enemy":
                print("SIDE COL")
                player.make_hit()
                # player.health += -1 
                # print("VIDA: {0}".format(player.health)) 
                
        if obj and obj.name == "fruit":
            obj.kill()
            print("fruta")
            # player.manage_points()
            SONIDO_FRUTA.play()
            
    for obj in to_check_vertical:
        if obj and obj.name == "enemy":
            # obj.kill()
            print("VERTICAL COL")
            
            player.make_hit()
    
        if obj and obj.name == "flag":
            print("FLAG")  
    

              
            
                
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png")

    block_size = 96
    # small_block = 64
    
    grupo_frutas = pygame.sprite.Group()
    grupo_frutas.add(Fruit(200, 600, 32, 32))
    grupo_frutas.add(Fruit(400, 300, 32, 32))
    
    # grupo_enemigos = pygame.sprite.Group()
    # grupo_enemigos.add(Enemy(600, 600, 32, 32))
    
    
    flag = Flag(block_size * 9,HEIGHT - block_size * 5,64)
    player = Player(100, 100, 50, 50)
    fire = Fire(150, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    enemigo = Enemy(600, HEIGHT - block_size - 68 , 52, 42)
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    wall = [Block(0, i * block_size, block_size)
        for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
    wall_der = [Block(WIDTH - block_size, i * block_size, block_size)
        for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 3, block_size), Block(block_size * 5, HEIGHT - block_size * 4, block_size), Block(block_size * 7, HEIGHT - block_size * 5, block_size), fire, *wall, *wall_der,*grupo_frutas]

    grupo_objectos = pygame.sprite.Group()
    
    grupo_objectos.add(*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 3, block_size), Block(block_size * 5, HEIGHT - block_size * 4, block_size), Block(block_size * 7, HEIGHT - block_size * 5, block_size), fire, *wall, *wall_der,*grupo_frutas, enemigo, flag)
    
    
    offset_x = 0
    scroll_area_width = 200
    
    run = True
    
    while run:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
                if event.key == pygame.K_RCTRL:
                    print("SHOOT")
                    player.make_shoot()
                    
                    

        for bala in player.bullets:  
            for obj in grupo_objectos:
                if pygame.sprite.collide_mask(bala, obj) and obj.name == "enemy":
                    # print("matado")
                    obj.kill()
                    bala.kill()
                elif pygame.sprite.collide_mask(bala, obj) and obj.name == "fire":
                    bala.kill()
                elif pygame.sprite.collide_mask(bala, obj) and obj.name == "block":
                    bala.kill() 

        player.loop(FPS)
        fire.loop()
        enemigo.loop()
                
        # for fruta in grupo_frutas:
        #     fruta.loop()
        #     # pygame.display.update()
                     
        
        handle_move(player, grupo_objectos)
        draw(window, background, bg_image, player, grupo_objectos, offset_x)
        
        # current_fps = clock.get_fps()
        # print("FPS: ", current_fps)
        clock.tick(FPS)

        # movimiento nivel
        # if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
        #         (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
        #     offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
