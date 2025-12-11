import pygame
from settings import Settings
from formencode import MenuScene  # deine Start-Scene

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.bildschirm_breite, self.settings.bildschirm_hoehe)
        )
        pygame.display.set_caption("Rogue-like RPG")
        self.clock = pygame.time.Clock()
        self.running = True

        # Aktive Scene
        self.current_scene = None

    def set_scene(self, scene):
        """Aktuelle Scene wechseln"""
        self.current_scene = scene
        self.current_scene.game = self  # Scene bekommt Zugriff auf Game

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.current_scene:
                    self.current_scene.handle_events(event)

            if self.current_scene:
                self.current_scene.update()
                self.current_scene.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.settings.fps)

        pygame.quit()
