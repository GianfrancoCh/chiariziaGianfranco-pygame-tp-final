import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox


class FormControls(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.txt1 = TextBox(master=self,x=50,y=50,w=WIDTH-150,h=125,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="CONTROLES",font="DroidSerif",font_size=100,font_color=BLACK)
        self.txt_a = TextBox(master=self,x=50,y=200,w=WIDTH-150,h=50,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="A para moverse a la izquierda",font="DroidSerif",font_size=50,font_color=BLACK)
        self.txt_d = TextBox(master=self,x=50,y=275,w=WIDTH-150,h=50,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="D para moverse a la derecha",font="DroidSerif",font_size=50,font_color=BLACK)
        self.txt_space = TextBox(master=self,x=50,y=350,w=WIDTH-150,h=50,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="SPACE para saltar",font="DroidSerif",font_size=50,font_color=BLACK)
        self.txt_j = TextBox(master=self,x=50,y=425,w=WIDTH-150,h=50,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="J para disparar",font="DroidSerif",font_size=50,font_color=BLACK)
        self.txt_esc = TextBox(master=self,x=50,y=500,w=WIDTH-150,h=50,color_background=None,color_border=None,image_background="assets/Background/Gray.png",text="ESC para pausar el juego",font="DroidSerif",font_size=50,font_color=BLACK)
        self.boton_go_back = Button(master=self,x=(WIDTH/2-75),y=575,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/close_2.png",on_click=self.on_click_boton_go_back,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.txt1,self.txt_a,self.txt_d,self.txt_space,self.txt_j,self.txt_esc,self.boton_go_back]

    def on_click_boton_go_back(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_settings(self, parametro):
        self.pb1.value += 1

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()