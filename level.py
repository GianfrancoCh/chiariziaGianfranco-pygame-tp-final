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
from pygame import font
from pygame.locals import *



window = pygame.display.set_mode((WIDTH, HEIGHT))


class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.boton_play = Button(master=self,x=250,y=250,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/menu/play.png",on_click="",on_click_param="",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton_play]
        self.levels = leer_archivo("levels.json")
        self.background, self.bg_image = get_background("Green.png")
        self.flag_nivel = True
        self.pausado = False
        block_size = 96
        self.duracion_nivel = 62
        self.tiempo_inicial = time.time()
        

        self.floor = [Block(i * block_size, HEIGHT - block_size, block_size)
                 for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
        self.wall = [Block(0, i * block_size, block_size)
                for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
        self.wall_der = [Block(WIDTH - block_size, i * block_size, block_size)
                    for i in range(-HEIGHT // block_size, (HEIGHT * 2) // block_size)]
        
        # self.flag = Flag(block_size * 10,HEIGHT - block_size * 5,64)

        if self.flag_nivel:

            aux_player = self.levels[0]["player"]
            self.player = Player(x=aux_player["x"],y=aux_player["y"],width=aux_player["width"],height=aux_player["height"])
           
            # aux_player = self.levels[0]["player"]
            # self.player = (x=100, y=100, width=50, height=50)
            # self.player = Player(x=aux_player["x"],y=aux_player["y"],width=aux_player["width"],height=aux_player["height"])
            # self.player = self.generate_player()

            self.grupo_frutas = pygame.sprite.Group()
            self.generate_frutas()

            self.grupo_enemigos = pygame.sprite.Group()
            self.generate_enemies()

            self.grupo_plataformas = pygame.sprite.Group()
            self.generate_platforms()
            
            self.grupo_trampas = pygame.sprite.Group()
            self.generate_trampas()
            
            self.flag = self.generate_flag()
            
            for self.trampa in self.grupo_trampas:
                self.trampa.on()
                
            # self.fire = Fire(block_size * 8, (HEIGHT - block_size * 5) - 64, 16, 32)

            self.grupo_objetos = pygame.sprite.Group()
            self.grupo_objetos.add(*self.floor,*self.wall,*self.wall_der,*self.grupo_enemigos,*self.grupo_frutas,self.flag,*self.grupo_trampas,*self.grupo_plataformas)

            self.flag_nivel = False



    def on_click_boton1(self, parametro):
        self.set_active(parametro)


    def generate_player(self):
        aux_player = self.levels[2]["player"]
        player = Player(x=aux_player["x"],y=aux_player["y"],width=aux_player["width"],height=aux_player["height"])


        return player

    def generate_frutas(self):
        fruits = self.levels[2]["fruits"]
        for fruit in fruits:
            self.grupo_frutas.add(Fruit(x=fruit["x"],y=fruit["y"], width=fruit["width"], height=fruit["height"]))
        
        return self.grupo_frutas


    def generate_enemies(self):
        enemies = self.levels[2]["enemies"]
        for enemy in enemies:
            self.grupo_enemigos.add(Enemy(x=enemy["x"],y=enemy["y"], width=enemy["width"], height=enemy["height"]))


    def generate_platforms(self):
        platforms = self.levels[2]["platforms"]
        for platform in platforms:
            self.grupo_plataformas.add(Block(x=platform["x"],y=platform["y"], size=platform["size"]))
            
    def generate_flag(self):
        aux_flag = self.levels[2]["flag"]
        flag = Flag(x=aux_flag["x"],y=aux_flag["y"], size=aux_flag["size"])
        
        return flag
        
    def generate_trampas(self):
        trampas = self.levels[2]["trampas"]
        for trampa in trampas:
            self.grupo_trampas.add(Fire(x=trampa["x"],y=trampa["y"], width=trampa["width"], height=trampa["height"]))
            
            

    def restart_level(self):

        # self.cronometro = 120
        # self.music = True
        self.tiempo_inicial = time.time()
        self.grupo_plataformas.empty()
        self.grupo_enemigos.empty()
        self.grupo_frutas.empty()
        self.grupo_trampas.empty()
        
        self.generate_frutas()
        self.generate_enemies()
        self.generate_platforms()
        self.generate_trampas()
        
        for self.trampa in self.grupo_trampas:
            self.trampa.on()
            
        self.grupo_objetos = pygame.sprite.Group()
        self.grupo_objetos.add(*self.floor,*self.wall,*self.wall_der,*self.grupo_enemigos,*self.grupo_frutas,self.flag,*self.grupo_trampas,*self.grupo_plataformas)
        self.flag_nivel = True


    def update(self, lista_eventos,keys,delta_ms):
 

        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                    self.player.jump()
                if event.key == pygame.K_j:
                    print("SHOOT")
                    self.player.make_shoot()
                    SONIDO_SHOT.play()
                if event.key == pygame.K_ESCAPE:
                    self.pausado = not self.pausado
    
    

        if self.pausado:

            window.fill(WHITE)
            draw_text = MENU_FONT.render("PAUSA", 1, BLACK)
            window.blit(draw_text, (WIDTH/2 -150, HEIGHT/2 - 200))
            
            pygame.display.update()

        else:

            for aux_widget in self.lista_widget:
                aux_widget.update(lista_eventos)
                  
            
            
            for bala in self.player.bullets:
                for obj in self.grupo_objetos:
                    if pygame.sprite.collide_mask(bala, obj) and obj.name == "enemy":

                        obj.kill()
                        bala.kill()
                    elif pygame.sprite.collide_mask(bala, obj) and obj.name == "fire":
                        bala.kill()
                    elif pygame.sprite.collide_mask(bala, obj) and obj.name == "block":
                        bala.kill()

            self.player.loop(FPS)

            for self.enemigo in self.grupo_enemigos:
                self.enemigo.loop()

            for self.trampa in self.grupo_trampas:
                self.trampa.loop()

            # for self.fruta in self.grupo_frutas:
            #     self.fruta.loop()

            #MANEJO TIEMPO
            tiempo_actual = time.time()
            self.tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            self.tiempo_restante = max(self.duracion_nivel - self.tiempo_transcurrido, 0)
            
            if self.tiempo_restante == 0:
                self.player.is_lose = True
            
            handle_move(self.player, self.grupo_objetos)
            
            if self.player.is_lose:

                aux_player = self.levels[0]["player"]
                self.set_active("form_lose")
                self.player.is_lose = False
                self.player.lives = 3
                self.player.rect = pygame.Rect(aux_player["x"], aux_player["y"], aux_player["width"], aux_player["height"])
                self.restart_level()
                self.active = False

            if len(self.grupo_frutas) == 0:
                self.player.has_all_fruit = True
                
                if self.player.is_win:
                
                    aux_player = self.levels[0]["player"]
                    self.set_active("form_win")
                    self.active = False
                    self.player.lives = 3 
                    self.player.rect = pygame.Rect(aux_player["x"], aux_player["y"], aux_player["width"], aux_player["height"])  
                            
                    self.restart_level()
                    self.player.is_win = False

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
        
        draw_text = MENU_FONT.render(str(int(self.tiempo_restante)), 1, BLACK) 
        window.blit(draw_text, (1050,0))

        self.player.draw(window, offset_x)
        # pygame.display.update()



