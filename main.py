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
from game_level1 import FormGameLevel1
from game_level2 import FormGameLevel2
from game_level3 import FormGameLevel3
from gui_lose import FormLose
from gui_win import FormWin
from gui_leaderboard import FormLeaderboard
from gui_levels import FormLevels


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("PYGAME GIAN")

window = pygame.display.set_mode((WIDTH, HEIGHT))

background, bg_image = get_background("Green.png")

pygame.mixer.music.load("sound/bg_music.mp3")

            
def main(window):
    clock = pygame.time.Clock()
    
    # small_block = 64
    offset_x = 0
    # scroll_area_width = 200
    run = True
    
    form_main_menu = FormMainMenu(name="form_main_menu",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=True,path_bg = "assets/gui/menu/bg.png")
    form_controls = FormControls(name="form_controls",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg = "assets/gui/rating/bg.png")
    form_settings = FormSettings(name="form_settings",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg = "assets/gui/rating/bg.png")
    form_level1 = FormGameLevel1(name="form_level1",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg = "assets/gui/rating/bg.png")
    form_level2 = FormGameLevel2(name="form_level2",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg = "assets/gui/rating/bg.png")
    form_level3 = FormGameLevel3(name="form_level3",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg = "assets/gui/rating/bg.png")
    form_lose = FormLose(name="form_lose",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg ="assets/gui/rating/bg.png")
    form_win = FormWin(name="form_win",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg ="assets/gui/rating/bg.png",lvl1=form_level1,lvl2=form_level2,lvl3=form_level3)
    form_leaderboard =FormLeaderboard(name="form_leaderboard",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg ="assets/gui/rating/bg.png")
    form_levels = FormLevels(name="form_levels",master_surface = window,x=0,y=0,w=WIDTH,h=HEIGHT,color_background=None,color_border=(255,0,255),active=False,path_bg ="assets/gui/bubble/bg.png")

   
    
    while run:
        
        lista_eventos = pygame.event.get()
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                run = False
                break

        aux_form_active = Form.get_active()
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        
        player = None
        grupo_objectos = None
        
        draw(window, background, bg_image, player, grupo_objectos, offset_x, aux_form_active, lista_eventos, keys, delta_ms)
        
        if form_settings.sound_enabled:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()
        
        current_fps = clock.get_fps()
                
        pygame.display.update() 
        
        

     
    quit()

# movimiento nivel
        # if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
        #         (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
        #     offset_x += player.x_vel
if __name__ == "__main__":
    main(WINDOW)
