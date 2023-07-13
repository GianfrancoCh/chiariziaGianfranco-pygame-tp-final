import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Label(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=WHITE,color_border=BLACK,image_background=None,text="Label",font="Arial",font_size=14,font_color=BLACK):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.text = text
        self.render()
        
    def render(self):
        super().render()
        

    def update(self,lista_eventos):
        self.render()

    

