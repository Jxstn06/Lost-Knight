class Settings:

    def __init__(self):
        self.screen_breite = 1280
        self.screen_hoehe = 720
        self.hintergrundFarbe = (0, 0, 0)
        self.fps = 30

        # Maze Größe
        self.maze_sizes = {'klein': (21, 21),
                           'mittel': (31, 31),
                           'groß': (41, 41)}
