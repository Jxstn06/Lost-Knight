import pygame


class Button:
    def __init__(self, x, y, breite, hoehe, text, font, color=(200, 200, 200), hover_color=(255, 255, 0)):
        self.rect = pygame.Rect(x, y, breite, hoehe)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color

    # Zeichnet den Button
    def draw(self, screen):
        # Maus Position
        mouse_pos = pygame.mouse.get_pos()
        # Boolean ob die Maus über dem Button ist
        is_hover = self.rect.collidepoint(mouse_pos)
        # Farbe wechselt je nach Maus Position
        pygame.draw.rect(screen, self.hover_color if is_hover else self.color, self.rect)
        text = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


    # Ein Event für die Funktion des Buttons
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)