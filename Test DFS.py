import random

def generate_maze(width, height):
    # Width und Height müssen ungerade sein
    maze = [["█"] * width for _ in range(height)]

    # Startpunkt
    start_x = 1
    start_y = 1

    # Bewegungsrichtungen: (dx, dy)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    def dfs(x, y):
        maze[y][x] = " "  # aktives Feld wird zum Gang

        random.shuffle(directions)  # zufällige Richtung

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # Prüfen ob Nachbar in Bounds und noch Wand
            if 1 <= nx < width-1 and 1 <= ny < height-1:
                if maze[ny][nx] == "█":  # unbesuchtes Feld
                    maze[y + dy//2][x + dx//2] = " "  # Wand dazwischen entfernen
                    dfs(nx, ny)

    dfs(start_x, start_y)
    return maze

generate_maze(5, 5)