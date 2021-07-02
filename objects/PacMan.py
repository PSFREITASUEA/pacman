import pygame as pygame
from pygame.surface import Surface


class PacMan:
    def __init__(self, position, lives):
        self.position = position
        self.lives = lives
        self.sprites = []
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.current_frame = 0
        self.initialize_sprites()
        self.speed = 1

    def move(self):
        if self.is_moving_up:
            self.position.y -= self.speed
        elif self.is_moving_down:
            self.position.y += self.speed
        elif self.is_moving_left:
            self.position.x -= self.speed
        elif self.is_moving_right:
            self.position += self.speed

    def draw(self, screen: Surface):
        screen.blit(self.sprites[self.current_frame], (self.position.x, self.position.y))

    def update(self):
        self.move()
        self.animate()

    def initialize_sprites(self):
        for number_sprite in range(1, 2):
            self.sprites.append(
                pygame.image.load(f'assets/pac_man_{number_sprite}'.png)
            )

    def animate(self):
        if self.current_frame == len(self.sprites):
            self.current_frame = 0
        if self.is_moving_up:
            self.current_frame += 0.25
        elif self.is_moving_down:
            self.current_frame += 0.25
        elif self.is_moving_left:
            self.current_frame += 0.25
        elif self.is_moving_right:
            self.current_frame += 0.25
