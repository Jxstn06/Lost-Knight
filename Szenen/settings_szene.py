import pygame

from Szenen.basis_szene import Scene


class SettingsScene(Scene):

    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.font = pygame.font.Font(None, 50)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.manager.set_state('menuszene')

    def draw(self):
        self.display.fill((0, 0, 50))
        text = self.font.render(
            "Settings - Press ESC to go back", True, (255, 255, 255)
        )
        self.display.blit(text, (50, 200))

    def run(self):
        self.draw()

