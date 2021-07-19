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
        self.surface.blit(sprite, position)

    def draw_maze(self, maze: Maze):
        for y_index in range(0, len(maze.cells)):
            for x_index in range(0, len(maze.cells[y_index])):
                cell_to_be_drawn = maze.cells[y_index][x_index]
                self.surface.blit(cell_to_be_drawn.sprite, cell_to_be_drawn.position)

    def draw_coins(self, coins):
        for coin in coins:
            self.surface.blit(coin.sprite, (coin.position[0], coin.position[1]))

    def draw_background(self):
        self.surface.fill((0, 0, 0))

    def draw_ghosts(self, ghosts):
        for ghost in ghosts:
            self.surface.blit(ghost.get_current_sprite(), ghost.get_current_position())
