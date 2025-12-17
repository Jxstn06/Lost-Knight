import pygame

class Spieler(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        # Spieler Position und größe des Sprites
        self.x = x
        self.y = y
        self.size = size
        self.update_spieler()


    def bewegung(self):
        self.update_spieler()

    def update_spieler(self):
        pass