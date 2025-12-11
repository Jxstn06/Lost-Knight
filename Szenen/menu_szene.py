import pygame
from Szenen.basis_szene import Scene
from Szenen.button import Button
from Szenen.newcharakter_szene import NewCharacterScene
from Szenen.loadcharakter_szene import LoadCharacterScene
from Szenen.settings_szene import SettingsScene
from settings import Settings


class MenuScene(Scene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.font = pygame.font.Font(None, 50)
        self.buttons = [
                        Button(300, 150, 200, 50, "New Character", self.font),
                        Button(300, 220, 200, 50, "Load Character", self.font),
                        Button(300, 290, 200, 50, "Settings", self.font),
                        Button(300, 360, 200, 50, "Quit", self.font)
                        ]

    def run(self):
        self.display.fill((0, 0, 0))
        for button in self .buttons:
            button.draw(self.display)
