import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox


class FormLose(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.txt1 = TextBox(master=self,x=150,y=50,w=WIDTH-250,h=300,color_background=None,color_border=None,image_background="assets/gui/you_lose/header.png",text="",font="DroidSerif",font_size=100,font_color=BLACK)
        self.boton_go_back = Button(master=self,x=(WIDTH/2-75),y=575,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/close.png",on_click=self.on_click_boton_go_back,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.txt1,self.boton_go_back]

    def on_click_boton_go_back(self, parametro):
        self.set_active(parametro)
        

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()