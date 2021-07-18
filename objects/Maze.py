from pygame.math import Vector2

from objects.Cell import Cell
from objects.Coin import Coin


class Maze:
    def __init__(self):
        self.walls = []
        self.spawn = 0
        self.coins = []
        self.ghost_spawns_cells = []
        self.load()

    def load(self):
        with open("assets/modified_maze.txt", 'r') as file:
            y = 0
            for yidx, line in enumerate(file):
                x = 0
                for xidx, char in enumerate(line):
                    if char == "0":
                        self.walls.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_{char}",
                                x_index=xidx,
                                y_index=yidx,
                                is_ghost_spawn=False))
                        self.coins.append((Coin(position=Vector2(x, y), x_index=xidx, y_index=yidx)))
                    elif char == "S":
                        self.walls.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_0",
                                x_index=xidx,
                                y_index=yidx,
                                is_ghost_spawn=False))
                    elif char == "L":
                        cell_to_be_created = Cell(
                            position=Vector2(x, y),
                            wall_type=f"wall_0",
                            x_index=xidx,
                            y_index=yidx,
                            is_ghost_spawn=True)
                        self.walls.append(cell_to_be_created)
                        self.ghost_spawns_cells.append(cell_to_be_created)
                    elif char != "\n":
                        self.walls.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_{char}",
                                x_index=xidx,
                                y_index=yidx,
                                is_ghost_spawn=False))

                    x += 32
                y += 32

    def get_spawn(self):
        for cell in self.walls:
            if cell.wall_type == "wall_0":
                self.spawn = cell
                return self.spawn

    def get_cell(self, x_index, y_index):
        for cell in self.walls:
            if cell.x_index == x_index and cell.y_index == y_index:
                return cell

    def update(self, x_index, y_index):
        for coin in self.coins:
            if coin.x_index == x_index and coin.y_index == y_index:
                self.coins.remove(coin)
                break
