import pygame


class Ghost:
    def __init__(self, spawn, difficult, color):
        self.color = color
        self.current_cell = spawn
        self.sprites_left = []
        self.current_frame_left = 0
        self.sprites_right = []
        self.current_frame_right = 0
        self.sprites_up = []
        self.current_frame_up = 0
        self.sprites_down = []
        self.current_frame_down = 0
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.initialize_sprites()
        self.time_to_move = 0.0

    def get_current_sprite(self):
        return self.sprites_right[int(self.current_frame_right)]

    def get_current_position(self):
        return self.current_cell.position

    def update(self, walls, player_cell):
        if int(self.time_to_move) == 1:
            self.move(walls, player_cell)
            self.time_to_move = 0.0
        else:
            self.time_to_move += 0.10

    def initialize_sprites(self):
        self.sprites_left.append(pygame.image.load(f'assets/{self.color}_ghost_left.png'))
        self.sprites_down.append(pygame.image.load(f'assets/{self.color}_ghost_down.png'))
        self.sprites_up.append(pygame.image.load(f'assets/{self.color}_ghost_up.png'))
        self.sprites_right.append(pygame.image.load(f'assets/{self.color}_ghost_right.png'))

    def move(self, walls, player_cell):
        self.current_cell = self.get_next_cell(walls, player_cell)

    def get_next_cell(self, walls, player_cell):
        next_cell = self.BFS(self.current_cell, walls, player_cell)
        return next_cell

    def BFS(self, start, walls, cell_target):
        target = [cell_target.x_index, cell_target.y_index]
        print(start.x_index, start.y_index)
        lines = len(walls)
        columns = len(walls[0])
        grid = [[0 for x in range(lines)] for x in range(columns)]

        for lines in walls:
            for cell in lines:
                if not cell.is_walkable_for_ghosts:
                    grid[cell.y_index][cell.x_index] = 1

        queue = [[start.x_index, start.y_index]]
        path = []
        visited = []

        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if 0 <= neighbour[0] + current[0] < len(grid[0]):
                        if 0 <= neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                grid_val = grid[next_cell[1]][next_cell[0]]
                                if grid_val != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})

        shortest = [target]
        while target != [start.x_index, start.y_index]:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])

        if len(shortest) == 1:
            shortest_cell_index_position = shortest[0]
        else:
            shortest_cell_index_position = shortest[1]
        next_cell = walls[shortest_cell_index_position[1]][shortest_cell_index_position[0]]
        return next_cell
