import pygame


class InputBox:
    def __init__(self, x, y, breite, hoehe, text, color=(200, 200, 200), hover_color=(255, 255, 0)):
        self.rect = pygame.Rect(x, y, breite, hoehe)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.color = color
        self.hover_color = hover_color


