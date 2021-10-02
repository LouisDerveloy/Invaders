import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.velocity = 10
        self.image = pygame.image.load("image/battleship_player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x #la largeur de x est 130
        self.rect.y = y #la largeur de y est 130

# sert a faire bouger le joueur
    def move_left(self):
        if not self.rect.x <= 0:
            self.rect.x -= self.velocity
    def move_right(self):
        if not self.rect.x >= 1920 - 130:
            self.rect.x += self.velocity
    def move_up(self):
        if not self.rect.y <= 0:
            self.rect.y -= self.velocity
    def move_down(self):
        if not self.rect.y >= 1080 - 130:
            self.rect.y += self.velocity