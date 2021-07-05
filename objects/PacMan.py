import pygame.image


class PacMan:
    def __init__(self, spawn):
        self.spawn = spawn
        self.position = spawn.position
        self.x_index = spawn.x_index
        self.y_index = spawn.y_index
        self.previous_cell = spawn
        self.sprite = pygame.image.load("assets/pac_man_right_1.png")
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def change_direction_to(self, direction):
        if direction == "LEFT":
            self.is_moving_left = True
            self.is_moving_right = False
            self.is_moving_up = False
            self.is_moving_down = False
        elif direction == "RIGHT":
            self.is_moving_left = False
            self.is_moving_right = True
            self.is_moving_up = False
            self.is_moving_down = False
        elif direction == "UP":
            self.is_moving_left = False
            self.is_moving_right = False
            self.is_moving_up = True
            self.is_moving_down = False
        elif direction == "DOWN":
            self.is_moving_left = False
            self.is_moving_right = False
            self.is_moving_up = False
            self.is_moving_down = True

    def increase_index(self):
        if self.is_moving_right:
            self.x_index += 0.25
        elif self.is_moving_up:
            self.y_index -= 0.25
        elif self.is_moving_down:
            self.y_index += 0.25
        elif self.is_moving_left:
            self.x_index -= 0.25

    def update(self, cell):
        self.increase_index()
        self.move(cell)

    def move(self, cell):
        if cell.wall_type != "wall_0":
            self.position = self.previous_cell.position
            self.x_index = self.previous_cell.x_index
            self.y_index = self.previous_cell.y_index
        else:
            self.previous_cell = cell
            self.position = cell.position
