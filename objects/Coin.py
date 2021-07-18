import pygame


class Coin:
    def __init__(self, position, x_index, y_index):
        self.position = position
        self.x_index = x_index
        self.y_index = y_index
        self.value = 10
        self.sprite = pygame.image.load("assets/coin.png")
