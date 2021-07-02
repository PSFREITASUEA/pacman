import pygame
from pygame import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

from objects.PacMan import PacMan
from objects.Screen import Screen


class Game:
    def __init__(self, screen_width, screen_height, framerate):
        self.screen = Screen(screen_width, screen_height)
        self.is_running = True
        self.pac_man = PacMan((self.screen.get_screen_width() / 2, self.screen.get_screen_height() / 2), 3)
        self.framerate = framerate

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

            self.pac_man.update()
            self.screen.draw(self.pac_man.get_current_sprite(), self.pac_man.get_current_position())
            pygame.display.flip()
            self.screen.draw_background()

    def stop_game(self):
        self.is_running = False
