import pygame
from os import listdir
from os.path import isfile, join
from player import *
from constantes import *


pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Platformer")


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


def get_background(name):
    image = pygame.image.load(join("assets/Background", name))

    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x, aux_form_active, lista_eventos, keys, delta_ms):
    
    
    if aux_form_active is not None:
        aux_form_active.update(lista_eventos, keys, delta_ms)
        aux_form_active.draw()
    else:
        for tile in background:
            window.blit(bg_image, tile)

        for obj in objects:
            obj.draw(window, offset_x)

        player.draw(window, offset_x)

        for bullet in player.bullets:
            bullet.draw(window, offset_x)

    pygame.display.update()
            
    # draw_winner(str(player.score))
   


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


def draw_text(text,font, x, y, color):
    
    draw_text = font.render(text, 1, color)
    WINDOW.blit(draw_text, (x,y))
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
            player.make_win()