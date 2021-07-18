from pygame.math import Vector2

from objects.Cell import Cell
from objects.Coin import Coin


class Maze:
    def __init__(self):
        self.cells = []
        self.spawn = 0
        self.coins = []
        self.ghost_spawns_cells = []
        self.load()

    def load(self):
        with open("assets/modified_maze.txt", 'r') as file:
            y = 0
            for yidx, line in enumerate(file):
                x = 0
                line_cell = []
                for xidx, char in enumerate(line):
                    if char == "0":
                        line_cell.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_{char}",
                                is_ghost_spawn=False,
                                is_walkable=True))
                        self.coins.append((Coin(position=Vector2(x, y), x_index=xidx, y_index=yidx)))
                    elif char == "S":
                        line_cell.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_0",
                                is_ghost_spawn=False,
                                is_walkable=False))
                    elif char == "P":
                        line_cell.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_{char}",
                                is_ghost_spawn=False,
                                is_walkable=False))
                    elif char == "L":
                        cell_to_be_created = Cell(
                            position=Vector2(x, y),
                            wall_type=f"wall_0",
                            is_ghost_spawn=True,
                            is_walkable=False)
                        line_cell.append(cell_to_be_created)
                        self.ghost_spawns_cells.append(cell_to_be_created)
                    elif char != "\n":
                        line_cell.append(
                            Cell(
                                position=Vector2(x, y),
                                wall_type=f"wall_{char}",
                                is_ghost_spawn=False,
                                is_walkable=False)
                        )

                    x += 32
                self.cells.append(line_cell)
                y += 32

    def update(self, x_index, y_index):
        for coin in self.coins:
            if coin.x_index == x_index and coin.y_index == y_index:
                self.coins.remove(coin)
                break

    def get_spawn(self):
        return self.cells[1][1]
