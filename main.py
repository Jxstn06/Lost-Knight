import pygame
from maze import Maze

if __name__ == '__main__':
    maze = Maze(20, 6)
    print(maze.draw_grid())