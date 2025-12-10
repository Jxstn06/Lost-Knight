import random as r
from feld import Feld

class Maze:
    def __init__(self, width, height):
        # Größe des Maze:
        # Breite, Höhe - Es muss eine ungrade Zahl sein, weil das Grid bei 0 anfängt zu zählen.
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.cords = {
            # randrange garantiert einen ungraden Spawn
            'Spawn': [r.randrange(1, self.width, 2), r.randrange(1, self.height, 2)]
        }
        self.grid = [[Feld(x, y, 'Wand') for x in range(self.width)] for y in range(self.height)]
        self.startpunkt()
        self.weg_algorithmus()

    def startpunkt(self):
        start_x, start_y = self.cords['Spawn']
        self.grid[start_y][start_x].feldtyp = 'Spawn'

    def weg_algorithmus(self):
        richtungen = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        start_x, start_y = self.cords['Spawn']

        stack = [(start_x, start_y)]
        visited = set()
        visited.add((start_x, start_y))

        while stack:
            x, y = stack[-1]
            # Damit der Spawn bleibt
            self.grid[y][x].feldtyp = 'Weg' if (x, y) != (start_x, start_y) else 'Spawn'

            # Liste der Nachbarn, die noch unbesucht sind
            nachbarn = []
            for richtung_x, richtung_y in richtungen:
                Nachbar_x, Nachbar_y = x + richtung_x, y + richtung_y
                # Ist der Schritt überhaupt möglich?
                if 0 < Nachbar_x < self.width and 0 < Nachbar_y < self.height and (Nachbar_x, Nachbar_y) not in visited:
                    if self.grid[Nachbar_y][Nachbar_x].feldtyp == 'Wand':
                        nachbarn.append((Nachbar_x, Nachbar_y))

            if nachbarn:
                # Zufälligen Nachbar
                Nachbar_x, Nachbar_y = r.choice(nachbarn)
                # Wand zwischen x,y und Nachbar_x,Nachbar_y entfernen
                self.grid[y + (Nachbar_y - y)//2][x + (Nachbar_x - x)//2].feldtyp = 'Weg'
                visited.add((Nachbar_x, Nachbar_y))
                stack.append((Nachbar_x, Nachbar_y))
            else:
                # Sackgasse
                stack.pop()

    def draw_grid(self):
        drawGrid = ''
        for i in self.grid:  # Spalten
            for j in i:      # Zeilen
                match j.feldtyp:
                    case 'Wand':
                        drawGrid += '█'
                    case 'Spawn':
                        drawGrid += 'S'
                    case 'Weg':
                        drawGrid += ' '
                    case _:
                        drawGrid += '?'
            drawGrid += '\n'
        return drawGrid