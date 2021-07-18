import pygame.image


class Cell:
    def __init__(self, wall_type, position, is_ghost_spawn, is_walkable):
        self.wall_type = wall_type
        self.position = position
        self.sprite = pygame.image.load(f"assets/{wall_type}.png")
        self.is_ghost_spawn = is_ghost_spawn
        self.is_walkable = is_walkable
