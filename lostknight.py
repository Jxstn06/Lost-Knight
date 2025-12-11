import pygame
from settings import Settings
from manager import Manager
from Szenen.menu_szene import MenuScene
from Szenen.button import Button
from Szenen.basis_szene import Scene


class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_breite, self.settings.screen_hoehe))
        self.clock = pygame.time.Clock()

        self.manager = Manager('menuszene')
        self.menuszene = MenuScene(self.screen, self.manager)
        self.level = Level(self.screen, self.manager)

        self.states = {'menuszene': self.menuszene,
                       'level': self.level}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # Event wird an Szene weitergegeben
                self.states[self.manager.get_state()].handle_events(event)
            # Läuft die aktuelle Szene
            self.states[self.manager.get_state()].run()
            pygame.display.update()
            self.clock.tick(self.settings.fps)


# Test für den Szenen wechsel
class Level(Scene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager

    def run(self):
        self.display.fill('blue')
