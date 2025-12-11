import pygame
from basis_szene import Scene
from button import Button
from newcharakter_szene import NewCharacterScene
from loadcharakter_szene import LoadCharacterScene
from settings_szene import SettingsScene


class MenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 50)
        self.buttons = [
            Button(300, 150, 200, 50, "New Character", self.font),
            Button(300, 220, 200, 50, "Load Character", self.font),
            Button(300, 290, 200, 50, "Settings", self.font),
            Button(300, 360, 200, 50, "Quit", self.font)
        ]

    def handle_events(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                if button.text == "New Character":
                    self.lostknight.set_scene(NewCharacterScene())
                elif button.text == "Load Character":
                    self.lostknight.set_scene(LoadCharacterScene())
                elif button.text == "Settings":
                    self.lostknight.set_scene(SettingsScene())
                elif button.text == "Quit":
                    self.lostknight.running = False

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for button in self .buttons:
            button.draw(screen)
