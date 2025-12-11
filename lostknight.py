import pygame
from settings import Settings
from maze import Maze
from spieler import Spieler

# Spielklasse
class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_breite, self.settings.screen_hoehe))
        # FPS cap hilft bei CPU Belastung
        self.clock = pygame.time.Clock()
        self.running = True

    def szene(self):
        pass

    def handle_events(self):
        # Fenster schließen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        pass
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()