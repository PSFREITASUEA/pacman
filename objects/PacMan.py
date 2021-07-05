import pygame.image


class PacMan:
    def __init__(self, spawn):
        self.spawn = spawn
        self.position = spawn.position
        self.x_index = spawn.x_index
        self.y_index = spawn.y_index
        self.previous_cell = spawn
        self.sprite = pygame.image.load("assets/pac_man_right_1.png")

    def change_direction_to(self, direction):
        if direction == "LEFT":
            self.x_index -= 1
        elif direction == "RIGHT":
            self.x_index += 1
        elif direction == "UP":
            self.y_index -= 1
        elif direction == "DOWN":
            self.y_index += 1

    def move(self, cell):
        if cell.wall_type != "wall_0":
            self.position = self.previous_cell.position
            self.x_index = self.previous_cell.x_index
            self.y_index = self.previous_cell.y_index
        else:
            self.previous_cell = cell
            self.position = cell.position
