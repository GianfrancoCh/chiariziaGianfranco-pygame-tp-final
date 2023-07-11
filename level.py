import pygame
from auxiliar import *
from constantes import *
from object import *
from enemy import *
from bullet import Bullet
from player import Player
from gui_button import Button
from gui_form import Form
from gui_widget import Widget


window = pygame.display.set_mode((WIDTH, HEIGHT)) 


class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)


        self.boton_play = Button(master=self,x=250,y=250,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/menu/play.png",on_click="",on_click_param="",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton_play]
        
        # --- GAME ELEMNTS --- 
        
        
        
        self.background, self.bg_image = get_background("Green.png")

        block_size = 96

        self.player = Player(block_size + 50, HEIGHT - block_size -100, 50, 50)
        
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) 
                 for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
        wall = [Block(0, i * block_size, block_size) 
                for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
        wall_der = [Block(WIDTH - block_size, i * block_size, block_size) 
                    for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
        flag = Flag(block_size * 10,HEIGHT - block_size * 5,64)
        grupo_frutas = pygame.sprite.Group()
        grupo_frutas.add(Fruit(850, HEIGHT - block_size - 68, 32, 32))
        grupo_frutas.add(Fruit(400, 300, 32, 32))
        
        self.fire = Fire(block_size * 8, (HEIGHT - block_size * 5) - 64, 16, 32)
        
        self.enemigo = Enemy(600, HEIGHT - block_size - 68 , 52, 42)
        self.grupo_objetos = pygame.sprite.Group()
        self.grupo_objetos.add(*floor,*wall,*wall_der,self.enemigo,*grupo_frutas,flag,
                               Block(block_size * 3, HEIGHT - block_size * 3, block_size), 
                               Block(block_size * 4, HEIGHT - block_size * 3, block_size),
                               Block(block_size * 5, HEIGHT - block_size * 3, block_size), 
                               Block(block_size * 7, HEIGHT - block_size * 5, block_size),
                               Block(block_size * 8, HEIGHT - block_size * 5, block_size),
                               self.fire)
        
        self.fire.on()
        
        
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))

        

    def update(self, lista_eventos,keys,delta_ms):
        
        
        
        
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                    self.player.jump()
                if event.key == pygame.K_j:
                    print("SHOOT")
                    self.player.make_shoot()
                    
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
            
        for bala in self.player.bullets:  
            for obj in self.grupo_objetos:
                if pygame.sprite.collide_mask(bala, obj) and obj.name == "enemy":
                    # print("matado")
                    obj.kill()
                    bala.kill()
                elif pygame.sprite.collide_mask(bala, obj) and obj.name == "fire":
                    bala.kill()
                elif pygame.sprite.collide_mask(bala, obj) and obj.name == "block":
                    bala.kill() 
                    
        
        

        
        
        self.player.loop(FPS)
        self.enemigo.loop()
        self.fire.loop()
        handle_move(self.player, self.grupo_objetos)
        
        if self.player.is_win:
            print("GANO")
            
        if self.player.is_lose:
            self.active = False
            self.set_active("form_main_menu")

 

    def draw(self): 
        super().draw()
        
        offset_x = 0
        
        for tile in self.background:
            window.blit(self.bg_image, tile)
            
        for obj in self.grupo_objetos:
            obj.draw(window, offset_x)
            
        for bullet in self.player.bullets:
            bullet.draw(window,offset_x)
        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
            
        self.player.draw(window, offset_x)
        self.player.draw
        # pygame.display.update()
        
        
            
   