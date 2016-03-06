import os
from block import Block
from ball import Ball
from paddle import Paddle

class Board:

    def __init__(self, window):

        self.window = window
        self.h, self.w = window.getmaxyx()

        cells_x = self.w / Block.WIDTH
        cells_y = self.h / Block.HEIGHT
        self.field = [[None] * cells_x  for i in range(cells_y)]

        self._gen_blocks()
        self.ball = Ball(self.h-2, self.w/2)

        self.paddle = Paddle(self.h-1, self.w/2)

    def draw(self):
        for row in self.field:
            for cell in row:
                if cell is not None:
                    cell.draw(self.window)

        self.ball.draw(self.window)
        self.paddle.draw(self.window)

    def move(self, offset):
        self.paddle.move(offset, self.w)

    def animate(self):
        self.ball.animate()
        self._collide_blocks()

    def _collide_blocks(self):
        pass

    def _get_directories(self):
        return [f for f in os.listdir('.') if not os.path.isfile(f)]

    def _get_files(self):
        return [f for f in os.listdir('.') if os.path.isfile(f)]

    def _add_block(self, f):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell is None:
                    b = Block(f, y, x)
                    self.field[y][x] = b
                    return

    def _gen_blocks(self):
        for f in self._get_files():
            self._add_block(f)

        for f in self._get_directories():
            self._add_block(f)

