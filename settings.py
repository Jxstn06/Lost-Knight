class Settings:

    def __init__(self):
        self.screen_breite = 775
        self.screen_hoehe = 775
        self.hintergrundFarbe = (0, 0, 0)
        self.fps = 60

        # Maze Größe
        self.maze_sizes = {'klein': (21, 21), 'mittel': (31, 31), 'groß': (41, 41)}
