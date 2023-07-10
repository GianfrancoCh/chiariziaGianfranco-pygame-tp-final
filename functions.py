import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
import time
from player import *
from auxiliar import *
from object import *
from enemy import *
from constantes import *
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Platformer")


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
    




            
def main(WINDOW):
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
        
        
        # draw_text("PLAY", MENU_FONT, WIDTH/2 - 60, HEIGHT/2,WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
                if event.key == pygame.K_LCTRL:
                    print("SHOOT")
                    player.make_shoot()
               
        pygame.display.update()          
      
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
                
        
        handle_move(player, grupo_objectos)
        draw(WINDOW, background, bg_image, player, grupo_objectos, offset_x)
        
        #------------------------------
        # current_fps = clock.get_fps()
        # print("FPS: ", current_fps)
        clock.tick(FPS)
        
        # for fruta in grupo_frutas:
        #     fruta.loop()
        #     # pygame.display.update()
                     
        
        # movimiento nivel
        # if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
        #         (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
        #     offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(WINDOW)
