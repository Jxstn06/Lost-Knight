import pygame
import sys

from Szenen.basis_szene import Scene
from Szenen.button import Button
from settings import Settings


class MenuScene(Scene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.font = pygame.font.Font(None, 30)
        self.buttons = [
                        Button((self.settings.screen_breite/2)-100, 150, 200, 50, 'New Character', self.font),
                        Button((self.settings.screen_breite/2)-100, 220, 200, 50, 'Load Character', self.font),
                        Button((self.settings.screen_breite/2)-100, 290, 200, 50, 'Settings', self.font),
                        Button((self.settings.screen_breite/2)-100, 360, 200, 50, 'Quit', self.font)
                        ]

    def on_button_click(self, text):
        if text == 'New Character':
            self.manager.set_state('newcharakterszene')
        elif text == 'Load Character':
            self.manager.set_state('loadcharakterszene')
        elif text == 'Settings':
            self.manager.set_state('settingsszene')
        elif text == 'Quit':
            pygame.quit()
            sys.exit()

    def handle_events(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                self.on_button_click(button.text)

    def run(self):
        self.display.fill(self.settings.hintergrundFarbe)
        for button in self .buttons:
            button.draw(self.display)
