import pygame.image


class Cell:
    def __init__(self, wall_type, x_index, y_index, position):
        self.wall_type = wall_type
        self.position = position
        self.x_index = x_index
        self.y_index = y_index
        self.sprite = pygame.image.load(f"assets/{wall_type}.png")
