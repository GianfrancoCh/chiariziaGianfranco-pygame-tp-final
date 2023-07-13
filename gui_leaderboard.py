import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox
from gui_label import Label
from sqlite import Sql



class FormLeaderboard(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.num_nivel = 0
        self.tiempo = 9
        
        self.txt1 = TextBox(master=self,x=100,y=50,w=WIDTH-225,h=125,color_background=None,color_border=None,image_background="assets/gui/level_select/table.png",text="LEADERBOARD",font="DroidSerif",font_size=100,font_color=BLACK)
        self.pos_1 = Label(master=self,x=400,y=225,w=500,text=f"1- XXX - XXX",color_border=None,font="Verdana",font_size=35,font_color=BLACK)
        self.pos_2 = Label(master=self,x=400,y=325,w=500,text=f"2- XXX - XXX",color_border=None,font="Verdana",font_size=35,font_color=BLACK)
        self.pos_3 = Label(master=self,x=400,y=425,w=500,text=f"3- XXX - XXX",color_border=None,font="Verdana",font_size=35,font_color=BLACK)
        self.boton_go_back = Button(master=self,x=(WIDTH/2-75),y=575,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/close.png",on_click=self.on_click_boton_go_back,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.txt1,self.boton_go_back,self.pos_1,self.pos_2,self.pos_3]

    def on_click_boton_go_back(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos,keys,delta_ms):
        
        jugadores = Sql.devolver_puntaje()
        jugadores_leaderboard = []
            
        for i, jugador in enumerate(jugadores):
            jugador_string = f"{i+1}- {jugador[0]} - {jugador[1]} - Nivel {jugador[2]}"
            jugadores_leaderboard.append(jugador_string)   
            
        self.pos_1._text = jugadores_leaderboard[0]
        self.pos_2._text = jugadores_leaderboard[1]
        self.pos_3._text = jugadores_leaderboard[2]
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
            
    def probar_scoreboard(self,lista_sb,label,order,posicion_array,): 
           
        try:
            Label._text = f"{order}- {lista_sb[posicion_array][0]} - {int(lista_sb[posicion_array][1])}"
        except:
            pass

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()