import pygame

from Szenen.basis_szene import Scene
from Szenen.button import Button
from Szenen.inputbox import InputBox
from settings import Settings


class NewCharacterScene(Scene):

    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.settings = Settings()

        self.font = pygame.font.Font(None, 50)
        self.buttons = [
            Button((self.settings.screen_breite/2)-100, (self.settings.screen_hoehe/8)*6, 200, 50, 'Create')
            ]
        self.inputboxen = [
            InputBox((self.settings.screen_breite/2)-100, (self.settings.screen_hoehe/8)*5, 200, 50)
            ]

    def on_button_click(self, text):
        if text == 'Create':
            name = self.inputboxen[0].get_value()
            print(f"Dein Name ist: {name}")

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.manager.set_state('menuszene')

        # Button Inputs
        for inputs in self.inputboxen:
            if hasattr(inputs, 'handle_events'):
                inputs.handle_events(event)
        for button in self.buttons:
            if button.is_clicked(event):
                self.on_button_click(button.text)

    def run(self):
        self.display.fill(self.settings.hintergrundFarbe)
        for button in self .buttons:
            button.draw(self.display)
        for inputbox in self.inputboxen:
            inputbox.draw(self.display)
