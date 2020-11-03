import pygame

class IA(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity = 7
        self.image = pygame.image.load("image/battleship_IA.png")
        self.rect = self.image.get_rect()
        self.rect.x = x  # la largeur de x est 130
        self.rect.y = y  # la largeur de y est 130

        # sert a faire bouger l'IA !
    def move_down(self):
        self.rect.y += self.velocity