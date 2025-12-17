import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Text Input Boxes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)

# Font
font = pygame.font.Font(None, 50)


# TextBox class
class TextBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = ""
        self.cursor_pos = 0
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active if clicked
            self.active = self.rect.collidepoint(event.pos)
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.cursor_pos > 0:
                    self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]
                    self.cursor_pos -= 1
            elif event.key == pygame.K_DELETE:
                self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos + 1:]
            elif event.key == pygame.K_RETURN:
                print("Entered text:", self.text)
                self.text = ""
                self.cursor_pos = 0
            elif event.key == pygame.K_LEFT:
                if self.cursor_pos > 0:
                    self.cursor_pos -= 1
            elif event.key == pygame.K_RIGHT:
                if self.cursor_pos < len(self.text):
                    self.cursor_pos += 1
            else:
                self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                self.cursor_pos += len(event.unicode)

    def update(self, dt):
        if self.active:
            self.cursor_timer += dt
            if self.cursor_timer >= 500:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0
        else:
            self.cursor_visible = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color if not self.active else BLUE, self.rect, 2)
        text_surface = font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw cursor
        if self.cursor_visible and self.active:
            cursor_x = font.size(self.text[:self.cursor_pos])[0] + self.rect.x + 5
            pygame.draw.line(surface, BLACK, (cursor_x, self.rect.y + 5),
                             (cursor_x, self.rect.y + 5 + font.get_height()), 2)


# Create multiple text boxes
text_boxes = [
    TextBox(50, 50, 300, 50),
    TextBox(50, 150, 300, 50),
    TextBox(50, 250, 300, 50),
]

clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Send events to all text boxes
        for box in text_boxes:
            box.handle_event(event)

    # Update and draw all text boxes
    for box in text_boxes:
        box.update(dt)
        box.draw(screen)

    pygame.display.flip()

pygame.quit()

