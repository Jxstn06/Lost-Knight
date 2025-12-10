import random as r

class Feld:
    def __init__(self, x, y, feldtyp='Wand'):
        self.x = x
        self.y = y
        self.feldtyp = feldtyp


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid()

    def create_grid(self):
        grid = []
        for y in range(self.height):
            zeile = []
            for x in range(self.width):
                zeile.append(Feld(x, y, 'Wand'))  # alles Wand
            grid.append(zeile)
        return grid

    def grid_control(self):
        print(self.grid)


    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].feldtyp == 'Wand':
                    s += "██"
                else:
                    s += "  "
            s += "\n"
        return s
    #Maze anzeigen

# ------------------------
# Testen
# ------------------------
maze = Maze(15, 6)

print(maze)