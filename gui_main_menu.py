import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox



class FormMainMenu(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,path_bg):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,path_bg)

        self.welcome = TextBox(master=self,x=150,y=100,w=WIDTH-250,h=125,color_background=None,color_border=None,image_background="assets/gui/match3/down.png",text="PINKMAN ADVENTURE",font="DroidSerif",font_size=75,font_color=WHITE)
        self.boton_play = Button(master=self,x=250,y=HEIGHT - 300,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/menu/play.png",on_click=self.on__click_boton_play,on_click_param="form_level1",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_control = Button(master=self,x=550,y=HEIGHT - 300,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/menu/leader.png",on_click=self.on_click_boton_control,on_click_param="form_controls",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_leaderboard = Button(master=self,x=850,y=HEIGHT - 300,w=150,h=150,color_background=None,color_border=None,image_background="assets/gui/menu/prize.png",on_click=self.on_click_boton_leaderboard,on_click_param="form_leaderboard",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_settings = Button(master=self,x=WIDTH-100,y= 50,w=75,h=75,color_background=None,color_border=None,image_background="assets/gui/menu/setting.png",on_click=self.on_click_boton_settings,on_click_param="form_settings",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.boton_quit = Button(master=self,x=WIDTH-100,y=HEIGHT-100,w=50,h=50,color_background=None,color_border=None,image_background="assets/gui/btn/close.png",on_click=self.on_click_boton_quit,on_click_param="form_main_menu",text=None,font="DroidSerif",font_size=30,font_color=WHITE)
        self.lista_widget = [self.welcome,self.boton_play,self.boton_control,self.boton_leaderboard,self.boton_settings,self.boton_quit]

    
    def on__click_boton_play(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_control(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton_leaderboard(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_settings(self, parametro):
        self.set_active(parametro)
        
    def on_click_boton_quit(self, parametro):
        quit()        
        
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()