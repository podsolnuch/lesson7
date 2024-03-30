import pygame


class Block:
    def __init__(self, width, height, color=(255, 255, 255)):
        self.width, self.height = width, height
        self.color = color
        self.surface = pygame.Surface()
        self.rect = self.surface.get_ract()

    def get_position(self):
        return self.rect.x, self.rect.y

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_color(self, new_color: tuple[int, int, int]):
        self.color = new_color
        self.surface.fill(self.color)