import pygame
from pygame import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

from objects.Ghost import Ghost
from objects.Maze import Maze
from objects.PacMan import PacMan
from objects.Screen import Screen
from objects.Util import *


class Game:
    def __init__(self, screen_width, screen_height, framerate):
        self.screen = Screen(screen_width, screen_height)
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.is_running = True
        self.maze = Maze()
        self.pac_man = PacMan(self.maze.get_spawn())
        self.ghosts = []
        self.framerate = framerate
        self.generate_ghosts()

    def start_game(self):
        while self.is_running:
            self.screen.clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop_game()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.pac_man.change_direction_to("LEFT")
                    elif event.key == K_RIGHT:
                        self.pac_man.change_direction_to("RIGHT")
                    elif event.key == K_UP:
                        self.pac_man.change_direction_to("UP")
                    elif event.key == K_DOWN:
                        self.pac_man.change_direction_to("DOWN")

            for ghost in self.ghosts:
                ghost.update()


            self.screen.draw_background()
            self.screen.draw_maze(self.maze)
            self.pac_man.update(self.maze.cells)
            self.screen.draw_ghosts(self.ghosts)
            self.screen.draw_coins(self.maze.coins)
            self.screen.draw(self.pac_man.get_current_sprite(), self.pac_man.current_cell.position)
            self.maze.update(int(self.pac_man.x_index), int(self.pac_man.y_index))

            pygame.display.flip()

    def stop_game(self):
        self.is_running = False

    def generate_ghosts(self):
        for i in range(0, len(self.maze.ghost_spawns_cells)):
            self.ghosts.append(Ghost(self, vec(self.maze.ghost_spawns_cells[i].position), i))
