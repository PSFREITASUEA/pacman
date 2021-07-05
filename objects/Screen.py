import pygame

from objects.Maze import Maze


class Screen:
    def __init__(self, screen_width, screen_height):
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

    def get_screen_width(self):
        return self.surface.get_width()

    def get_screen_height(self):
        return self.surface.get_height()

    def draw(self, sprite, position):
        self.surface.blit(sprite, (position[0], position[1]))

    def draw_maze(self, maze: Maze):
        for wall in maze.walls:
            self.surface.blit(wall.sprite, (wall.position[0], wall.position[1]))

    def draw_background(self):
        self.surface.fill((0, 0, 0))
