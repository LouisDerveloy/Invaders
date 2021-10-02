import pygame
class image(pygame.sprite.Sprite):
    def __init__(self,url,axe_x,axe_y):
        super().__init__()
        self.image=pygame.image.load(url)
        self.rect=self.image.get_rect()
        self.rect.x =axe_x
        self.rect.y =axe_y
#base x=400
#base y=160
    def move_left(self,combien):
        self.rect.x=self.rect.x-combien
    def move_right(combien):
        self.rect.x=self.rect.x+combien
    def move_up(self, combien):
        self.rect.y=self.rect.y-combien
    def move_down(self, combien):
        self.rect.y=self.rect.y+combien