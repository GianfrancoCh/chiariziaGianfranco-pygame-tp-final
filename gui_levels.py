import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox



class FormLevels(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.welcome = TextBox(master=self,x=150,y=100,w=WIDTH-250,h=125,color_background=None,color_border=None,image_background="assets/gui/level_select/table.png",text="NIVELES",font="DroidSerif",font_size=75,font_color=BLACK)
        self.boton_level1 = Button(master=self,x=250,y=HEIGHT - 350,w=150,h=150,color_background=None,color_border=None,image_background="assets/Menu/Levels/01.png",on_click=self.on__click_boton_level1,on_click_param="form_level1",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_level2 = Button(master=self,x=550,y=HEIGHT - 350,w=150,h=150,color_background=None,color_border=None,image_background="assets/Menu/Levels/02.png",on_click=self.on_click_boton_level2,on_click_param="form_level2",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_level3 = Button(master=self,x=850,y=HEIGHT - 350,w=150,h=150,color_background=None,color_border=None,image_background="assets/Menu/Levels/03.png",on_click=self.on_click_boton_level3,on_click_param="form_level3",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_back = Button(master=self,x=WIDTH-150,y=HEIGHT-150,w=50,h=50,color_background=None,color_border=None,image_background="assets/gui/btn/prew.png",on_click=self.on_click_boton_back,on_click_param="form_main_menu",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.lista_widget = [self.welcome,self.boton_level1,self.boton_level2,self.boton_level3,self.boton_back]

    
    def on__click_boton_level1(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_level2(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton_level3(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_back(self, parametro):
        self.set_active(parametro)       
        
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()