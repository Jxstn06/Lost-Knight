import pygame
import sys

from Szenen.loadcharakter_szene import LoadCharacterScene
from Szenen.settings_szene import SettingsScene
from settings import Settings
from manager import Manager
from Szenen.menu_szene import MenuScene
from Szenen.newcharakter_szene import NewCharacterScene


class LostKnight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_breite, self.settings.screen_hoehe))
        self.clock = pygame.time.Clock()
        self.running = True

        self.manager = Manager('menuszene')
        self.menuszene = MenuScene(self.screen, self.manager)
        self.newcharakterszene = NewCharacterScene(self.screen, self.manager)
        self.loadcharakterszene = LoadCharacterScene(self.screen, self.manager)
        self.settingsszene = SettingsScene(self.screen, self.manager)

        self.states = {'menuszene': self.menuszene,
                       'newcharakterszene': self.newcharakterszene,
                       'loadcharakterszene': self.loadcharakterszene,
                       'settingsszene': self.settingsszene}

    def run(self):
        while self.running:
            for event in pygame.event.get():
                # Fenster geschlossen
                if event.type == pygame.QUIT:
                    self.running = False
                self.states[self.manager.get_state()].handle_events(event)
            # Läuft die aktuelle Szene
            self.states[self.manager.get_state()].run()
            pygame.display.update()
            self.clock.tick(self.settings.fps)

        pygame.quit()
        sys.exit()
