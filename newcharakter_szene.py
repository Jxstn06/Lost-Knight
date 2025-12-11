import pygame
from basis_szene import Scene

class NewCharacterScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 50)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from menu_szene import MenuSzene
            self.lostknight.set_scene(MenuSzene())

    def draw(self, screen):
        screen.fill((0, 0, 50))
        text_surf = self.font.render("New Character - Press ESC to go back", True, (255, 255, 255))
        screen.blit(text_surf, (50, 200))
