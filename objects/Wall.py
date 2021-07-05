import pygame.image


class Wall:
    def __init__(self, wall_type, position):
        self.wall_type = wall_type
        self.position = position
        self.sprite = pygame.image.load(f"assets/{wall_type}.png")
