# -*- coding: utf-8 -*-

from random import choice

from game.constants import MOVE

from AbstractStrategy import AbstractStrategy

class RandomStrategy(AbstractStrategy):
    def prepare(self):
        self.positions = [(x, y) for x in xrange(self.game.width) for y in xrange(self.game.height)]

    def get_move(self):
        x, y = choice(self.positions)

        while True:
            move, field = self.evaluate(x, y)
            if move in (MOVE.OK, MOVE.OLD):
                self.positions.remove((x, y))
                return

