import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox
from sqlite import Sql


class FormWin(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg,lvl1,lvl2,lvl3):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.puntos = 0
        self.level = 1
        self.nivel = lvl1
        self.lvl1 = lvl1
        self.lvl2 = lvl2
        self.lvl3 = lvl3
      
        
        
        self.txt1 = TextBox(master=self,x=150,y=50,w=WIDTH-250,h=300,color_background=None,color_border=None,image_background="assets/gui/you_win/header.png",text="",font="DroidSerif",font_size=100,font_color=BLACK)
        self.boton_go_back = Button(master=self,x=(WIDTH/2-300),y=575,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/close.png",on_click=self.on_click_boton_go_back,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton_ok = Button(master=self,x=(WIDTH/2+100),y=575,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/ok.png",on_click=self.on_click_boton_ok,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.name_box = TextBox(master=self,x=350,y=400,w=500,h=70,color_background=WHITE,color_border=BLACK,image_background=None,text="Ingrese nombre:",font="DroidSerif",font_size=50,font_color=BLACK)
        self.lista_widget = [self.txt1,self.boton_go_back,self.boton_ok,self.name_box]

    def on_click_boton_go_back(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_ok(self, parametro):
        Sql.crear_tabla()
        Sql.actualizar_tabla(self.name_box._text,self.puntos,self.level)
        Sql.devolver_puntaje()
        self.set_active("form_main_menu")
        
    def update(self, lista_eventos,keys,delta_ms):
        
        if self.lvl1.score_fin != 0:
            self.level =  1
        elif self.lvl2.score_fin != 0:
            self.level = 2
            self.nivel = self.lvl2
        else:
            self.level = 3 
            self.nivel = self.lvl3
                        
        self.puntos = int(self.nivel.score_fin)
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()