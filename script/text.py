import pygame
class text:
    def __init__(self, contenue_text, taille, color):
        font=pygame.font.SysFont( "arial" ,  taille)
        self.text=font.render(str(contenue_text),  True, (color))
        print(pygame.font.get_fonts())