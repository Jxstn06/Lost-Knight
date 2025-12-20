import pygame

from Szenen.basis_szene import Scene
from Szenen.button import Button
from Szenen.inputbox import InputBox
from settings import Settings
from Mazeshit.maze import Maze

from LostKnightDB import Spieler


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
            InputBox((self.settings.screen_breite/2)-100, (self.settings.screen_hoehe/8)*1, 200, 50),
            InputBox((self.settings.screen_breite/2)-100, (self.settings.screen_hoehe/8)*3, 200, 50)
            ]

    def on_button_click(self, text):
        if text == 'Create':
            # Erstellung des Mazes für den Spieler
            mazegroesze = self.inputboxen[1].get_value()
            if mazegroesze not in self.settings.maze_sizes:
                print("Ungültige Größe!")
                return
            x, y = self.settings.maze_sizes[mazegroesze]
            maze_obj = Maze(x, y)
            maze = str(maze_obj.draw_grid())

            start_x, start_y = maze_obj.startpunkt()

            # Erstellung des Spielers

            name = self.inputboxen[0].get_value()
            Spieler(Name=name, Level=1, Leben=20, Kraft=3, Verteidigung=2, X=start_x, Y=start_y, Maze=maze)

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
                self.manager.set_state('menuszene')

    def run(self):
        self.display.fill(self.settings.hintergrundFarbe)
        for button in self .buttons:
            button.draw(self.display)
        for inputs in self.inputboxen:
            inputs.draw(self.display)
