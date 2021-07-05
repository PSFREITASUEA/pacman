from objects.Wall import Wall


class Maze:
    def __init__(self):
        self.walls = []
        self.load()

    def load(self):
        with open("assets/modified_maze.txt", 'r') as file:
            y = 0
            for yidx, line in enumerate(file):
                x = 0
                for xidx, char in enumerate(line):
                    if char != "0" and char != "\n" and char != "S":
                        self.walls.append(Wall(position=(x, y), wall_type=f"wall_{char}"))
                    x += 32
                y += 32

    def draw(self, surface):
        for wall in self.walls:
            surface.blit(wall.sprite, (wall.position[0], wall.position[1]))
