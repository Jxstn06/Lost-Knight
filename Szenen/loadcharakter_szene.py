import pygame
from Szenen.basis_szene import Scene


class LoadCharacterScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 50)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from Szenen.menu_szene import MenuSzene
            self.lostknight.set_scene(MenuSzene())

    def draw(self, screen):
        screen.fill((50,0,0))
        text_surf = self.font.render("Load Character - Press ESC to go back", True, (255,255,255))
        screen.blit(text_surf, (50, 200))
