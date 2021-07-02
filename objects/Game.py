import pygame
from pygame import KEYDOWN, K_LEFT, K_RIGHT, KEYUP, K_UP, K_DOWN

from objects.PacMan import PacMan


class Game:
    def __init__(self, screen_width, screen_height, framerate):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.is_running = True
        self.pac_man = PacMan((self.screen.get_width() / 2, self.screen.get_height() / 2), 3)
        self.clock = pygame.time.Clock()
        self.framerate = framerate

    def start_game(self):
        while self.is_running:
            self.clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop_game()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.pac_man.is_moving_left = True
                    elif event.key == K_RIGHT:
                        self.pac_man.is_moving_right = True
                    elif event.key == K_UP:
                        self.pac_man.is_moving_up = True
                    elif event.key == K_DOWN:
                        self.pac_man.is_moving_down = True

                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.pac_man.is_moving_left = False
                    elif event.key == K_RIGHT:
                        self.pac_man.is_moving_right = False
                    elif event.key == K_UP:
                        self.pac_man.is_moving_up = False
                    elif event.key == K_DOWN:
                        self.pac_man.is_moving_down = False

            self.pac_man.update()
            self.pac_man.draw(self.screen)
            pygame.display.flip()
            self.screen.fill((0, 0, 0))

    def stop_game(self):
        self.is_running = False
