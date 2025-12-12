import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 30)

spieler = [("Max", 100), ("Anna", 200), ("Tom", 150), ("Lara", 180),
           ("Ben", 90), ("Eva", 120), ("Leo", 300), ("Mia", 250),
           ("Tim", 60), ("Nina", 110), ("Paul", 95)]

BG_COLOR = (220, 220, 220)
ITEM_COLOR = (200, 200, 200)
HOVER_COLOR = (150, 150, 250)
TEXT_COLOR = (0, 0, 0)

ITEM_HEIGHT = 40
scroll_offset = 0
max_offset = max(0, len(spieler)*ITEM_HEIGHT - 300)  # 300 = sichtbare Höhe

running = True
while running:
    screen.fill(BG_COLOR)
    mouse_pos = pygame.mouse.get_pos()
    clicked_item = None

    # Zeichne Liste
    for i, (name, punkte) in enumerate(spieler):
        rect_y = 50 + i * ITEM_HEIGHT - scroll_offset
        rect = pygame.Rect(50, rect_y, 300, ITEM_HEIGHT - 5)

        # nur zeichnen, wenn sichtbar
        if rect.bottom < 50 or rect.top > 350:  # 50-350 = sichtbarer Bereich
            continue

        # Hover-effekt
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, rect)
            if pygame.mouse.get_pressed()[0]:
                clicked_item = i
        else:
            pygame.draw.rect(screen, ITEM_COLOR, rect)

        text = font.render(f"{name} - {punkte}", True, TEXT_COLOR)
        screen.blit(text, (rect.x + 10, rect.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mausrad scrollen
        if event.type == pygame.MOUSEWHEEL:
            scroll_offset -= event.y * ITEM_HEIGHT  # y=1 nach oben, y=-1 nach unten
            scroll_offset = max(0, min(scroll_offset, max_offset))  # Begrenzung

    if clicked_item is not None:
        print(f"Geklickt auf: {spieler[clicked_item][0]}")

    pygame.display.flip()

pygame.quit()