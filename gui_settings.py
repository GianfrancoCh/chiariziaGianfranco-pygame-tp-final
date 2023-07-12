import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox

class FormSettings(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.txt_settings = TextBox(master=self,x=150,y=50,w=WIDTH-250,h=300,color_background=None,color_border=None,image_background="assets/gui/settings/92.png",text="",font="DroidSerif",font_size=100,font_color=BLACK)
        self.txt_sound = TextBox(master=self,x=250,y=375,w=350,h=100,color_background=None,color_border=None,image_background="assets/gui/settings/93.png",text="SOUND:",font="DroidSerif",font_size=100,font_color=BLACK)
        self.boton_on = Button(master=self,x=700,y=400,w=150,h=50,color_background=None,color_border=None,image_background="assets/gui/settings/96.png",on_click=self.on_click_sound_on,on_click_param="",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton_off = Button(master=self,x=700,y=400,w=150,h=50,color_background=None,color_border=None,image_background="assets/gui/settings/95.png",on_click=self.on_click_sound_off,on_click_param="",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton_go_back = Button(master=self,x=(WIDTH/2-75),y=525,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/btn/close.png",on_click=self.on_click_boton_go_back,on_click_param="form_main_menu",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.txt_settings,self.txt_sound,self.boton_on,self.boton_go_back]

    def on_click_boton_go_back(self, parametro):
        self.set_active(parametro)

    def change_state_button(self, button_true, button_false):
        self.lista_widget.remove(button_true)
        self.lista_widget.append(button_false)    
    
    def on_click_sound_on(self, parametro):

        self.change_state_button(self.boton_on, self.boton_off)
        
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0)

    def on_click_sound_off(self, parametro):
        
        self.change_state_button(
            self.boton_off, self.boton_on)

        pygame.mixer.music.set_volume(1.0)
    
    
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()