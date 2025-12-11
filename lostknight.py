import pygame
from settings import Settings
from manager import Manager
from Szenen.menu_szene import MenuScene
from Szenen.button import Button


class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_breite, self.settings.screen_hoehe))
        self.clock = pygame.time.Clock()

        self.manager = Manager('start')
        self.start = MenuScene(self.screen, self.manager)
        self.level = Level(self.screen, self.manager)

        self.states = {'start': self.start,
                       'level': self.level
                        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # Event wird an Szene weitergegeben
                self.states[self.manager.get_state()].handle_events(event)

            self.states[self.manager.get_state()].run()
            pygame.display.update()
            self.clock.tick(self.settings.fps)


class Level:
    def __init__(self, display, manager):
        self.display = display
        self.manager = manager

    def handle_events(self, event):
        pass

    def run(self):
        self.display.fill('blue')


class Start:
    def __init__(self, display, manager):
        self.display = display
        self.manager = manager

    def run(self):
        self.display.fill('red')
