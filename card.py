import pygame


class Card:
    def __init__(self, color, val, x, y, screen):
        self.color = color
        self.val = val
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 20, 100))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
