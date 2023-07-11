import os
import random
import math
import pygame
import time
from player import Player
from object import *
from enemy import *
from constantes import *
from auxiliar import get_background, draw, handle_move
from pygame.locals import *
from gui_button import Button
from gui_form import *
from gui_widget import Widget
from gui_main_menu import FormMainMenu
from gui_controls import FormControls
from gui_settings import FormSettings




pygame.init()
pygame.mixer.init()
pygame.display.set_caption("PYGAME GIAN")

window = pygame.display.set_mode((WIDTH, HEIGHT))

background, bg_image = get_background("Green.png")

            
def main(window):
    clock = pygame.time.Clock()
    

    block_size = 96
    # small_block = 64
    # grupo_enemigos = pygame.sprite.Group()
    # # grupo_enemigos.add(Enemy(600, 600, 32, 32))
    #----------------------------------------------------------
    
    # grupo_frutas = pygame.sprite.Group()
    # grupo_frutas.add(Fruit(1000, 400, 32, 32))
    # grupo_frutas.add(Fruit(400, 300, 32, 32))
    # flag = Flag(block_size * 9,HEIGHT - block_size * 5,64)
    # player = Player(100, 100, 50, 50)
    # fire = Fire(150, HEIGHT - block_size - 64, 16, 32)
    # fire.on()
    # enemigo = Enemy(600, HEIGHT - block_size - 68 , 52, 42)
    
    # floor = [Block(i * block_size, HEIGHT - block_size, block_size)
    #          for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    # wall = [Block(0, i * block_size, block_size)
    #     for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
    # wall_der = [Block(WIDTH - block_size, i * block_size, block_size)
    #     for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
    # objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
    #            Block(block_size * 3, HEIGHT - block_size * 3, block_size), Block(block_size * 5, HEIGHT - block_size * 4, block_size), Block(block_size * 7, HEIGHT - block_size * 5, block_size), fire, *wall, *wall_der,*grupo_frutas]

    # grupo_objectos = pygame.sprite.Group()
    
    # grupo_objectos.add(*floor, Block(0, HEIGHT - block_size * 2, block_size),
    #            Block(block_size * 3, HEIGHT - block_size * 3, block_size), Block(block_size * 5, HEIGHT - block_size * 4, block_size), Block(block_size * 7, HEIGHT - block_size * 5, block_size), fire, *wall, *wall_der,*grupo_frutas, enemigo, flag)
    
    
    offset_x = 0
    # scroll_area_width = 200
    run = True
    
    
    
    form_main_menu = FormMainMenu(name="form_main_menu",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=True,path_bg = "assets/gui/menu/bg.png")
    form_controls = FormControls(name="form_controls",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=True,path_bg = "assets/gui/rating/bg.png")
    form_settings = FormSettings(name="form_settings",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=True,path_bg = "assets/gui/rating/bg.png")
    
    while run:
        
        
        # draw_text("PLAY", MENU_FONT, WIDTH/2 - 60, HEIGHT/2,WHITE)
        
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
                if event.key == pygame.K_j:
                    print("SHOOT")
                    player.make_shoot()
               
                
        # player.loop(FPS)
        # fire.loop()
        # enemigo.loop()

        # for bala in player.bullets:  
        #     for obj in grupo_objectos:
        #         if pygame.sprite.collide_mask(bala, obj) and obj.name == "enemy":
        #             # print("matado")
        #             obj.kill()
        #             bala.kill()
        #         elif pygame.sprite.collide_mask(bala, obj) and obj.name == "fire":
        #             bala.kill()
        #         elif pygame.sprite.collide_mask(bala, obj) and obj.name == "block":
        #             bala.kill() 
        
        # for fruta in grupo_frutas:
        #     fruta.loop()
        #     pygame.display.update()
        aux_form_active = Form.get_active()
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        
        player = None
        grupo_objectos = None
        
        
        # handle_move(player, grupo_objectos)
        draw(window, background, bg_image, player, grupo_objectos, offset_x, aux_form_active, lista_eventos, keys, delta_ms)
        
        
        
        #------------------------------
        # current_fps = clock.get_fps()
        # print("FPS: ", current_fps)
        
        
       
                     
        pygame.display.update() 
        
        # movimiento nivel
        # if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
        #         (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
        #     offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(WINDOW)
