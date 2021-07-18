import pygame.image


class PacMan:
    def __init__(self, spawn_cell):
        self.current_cell = spawn_cell
        self.sprite = pygame.image.load("assets/pac_man_right_1.png")
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.sprites_left = []
        self.current_frame_left = 0
        self.sprites_right = []
        self.current_frame_right = 0
        self.sprites_up = []
        self.current_frame_up = 0
        self.sprites_down = []
        self.current_frame_down = 0
        self.initialize_sprites()
        self.x_index = 1
        self.y_index = 1

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
            self.x_index += 0.10
        elif self.is_moving_up:
            self.y_index -= 0.10
        elif self.is_moving_down:
            self.y_index += 0.10
        elif self.is_moving_left:
            self.x_index -= 0.10

        if self.x_index >= 19:
            self.x_index = 19
        elif self.x_index <= 0:
            self.x_index = 0
        if self.y_index >= 19:
            self.y_index = 19
        elif self.y_index <= 0:
            self.y_index = 0

    def update(self, cells):
        self.increase_index()
        self.move(cells)

    def move(self, cells):
        if self.is_moving_right:
            if not cells[int(self.y_index)][int(self.x_index)].is_walkable:
                self.x_index -= 1
                self.is_moving_right = False
        elif self.is_moving_left:
            if not cells[int(self.y_index)][int(self.x_index)].is_walkable:
                self.x_index += 1
                self.is_moving_left = False
        elif self.is_moving_down:
            if not cells[int(self.y_index)][int(self.x_index)].is_walkable:
                self.y_index -= 1
                self.is_moving_down = False
        elif self.is_moving_up:
            if not cells[int(self.y_index)][int(self.x_index)].is_walkable:
                self.y_index += 1
                self.is_moving_up = False

        self.current_cell = cells[int(self.y_index)][int(self.x_index)]

    def initialize_sprites(self):
        for number_sprite in range(1, 3):
            self.sprites_left.append(
                pygame.image.load(f'assets/pac_man_left_{number_sprite}.png')
            )
        for number_sprite in range(1, 3):
            self.sprites_right.append(
                pygame.image.load(f'assets/pac_man_right_{number_sprite}.png')
            )
        for number_sprite in range(1, 3):
            self.sprites_up.append(
                pygame.image.load(f'assets/pac_man_up_{number_sprite}.png')
            )
        for number_sprite in range(1, 3):
            self.sprites_down.append(
                pygame.image.load(f'assets/pac_man_down_{number_sprite}.png')
            )

    def animate(self):
        if self.is_moving_left:
            self.current_frame_left += 0.10
            if self.current_frame_left >= len(self.sprites_left):
                self.current_frame_left = 0
        elif self.is_moving_down:
            self.current_frame_down += 0.10
            if self.current_frame_down >= len(self.sprites_down):
                self.current_frame_down = 0
        elif self.is_moving_right:
            self.current_frame_right += 0.10
            if self.current_frame_right >= len(self.sprites_right):
                self.current_frame_right = 0
        elif self.is_moving_up:
            self.current_frame_up += 0.10
            if self.current_frame_up >= len(self.sprites_up):
                self.current_frame_up = 0

    def get_current_sprite(self):
        if self.is_moving_left:
            return self.sprites_left[int(self.current_frame_left)]
        elif self.is_moving_down:
            return self.sprites_down[int(self.current_frame_down)]
        elif self.is_moving_right:
            return self.sprites_right[int(self.current_frame_right)]
        elif self.is_moving_up:
            return self.sprites_up[int(self.current_frame_up)]
        else:
            return self.sprites_right[int(self.current_frame_right)]
