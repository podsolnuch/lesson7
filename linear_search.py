import pygame
from pygame.event import Event

from game_objects import Block


class Window:
    _color_of_block_standard = (155, 155, 200)
    _color_of_block_current = (200, 155, 155)
    _color_of_block_found = (155, 200, 155)

    def __init__(self, width=800, height=600, sequence: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        pygame.init()
        self.width = width
        self.height = height
        self.surf = pygame.display.set_mode((self.width,self.height))
        self.surf_color = (0, 0, 0)
        self.surf.fill(self.surf_color)
        self.clock = pygame.time.Clock()
        self._running = False
        self.blocks = []
        self.sequence = sequence

    def spawn_block(self):
        block_width = self.width / len(self.sequence)
        block_height = self.height / max(self.sequence)
        x = 0
        for i in self.sequence:
            block = Block(block.width, block_height * i, self._color_of_block_standard)
            block.set_position(x, self.height - block.height)
            x = x + block_width
            self.blocks.append(block)

    def on_event(self, event: Event):
        if event.type == pygame.QUIT:
            self._running = False

    def render(self):
        self.surf.fill(self.surf_color)
        for block in self.blocks:
            self.surf.blit(block.surface, block.get_position())
        pygame.display.flip()

    def start(self):
        self.spawn_block()
        self._running = True
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.render()



my_window = Window(1024, 760)
my_window.start()
