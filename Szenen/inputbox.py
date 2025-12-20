import pygame


class InputBox:
    def __init__(self, x, y, breite, hoehe, text="", color=(200, 200, 200), clicked_color=(255, 255, 0)):
        self.rect = pygame.Rect(x, y, breite, hoehe)
        self.text = text
        self.font = pygame.font.Font(None, 30)

        # Color fix
        self.base_color = color
        self.clicked_color = clicked_color
        self.color = self.base_color

        self.active = False
        self.text_rect = self.font.render(text, True, (0, 0, 0))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.clicked_color if self.active else self.base_color

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < 12:
                self.text += event.unicode
        self.text_rect = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        # Text Hintergrund
        pygame.draw.rect(screen, self.base_color, self.rect)  # Grau
        # Inputbox Rahmen
        pygame.draw.rect(screen, self.clicked_color if self.active else (0, 0, 0), self.rect, 2)
        screen.blit(self.text_rect, (self.rect.x + 5, self.rect.y + 5))

    # Für den Datenbank Eintrag
    def get_value(self):
        return self.text



