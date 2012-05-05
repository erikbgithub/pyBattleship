# -*- coding: utf-8 -*-

from random import choice

from game.constants import MOVE, FIELD

from AbstractStrategy import AbstractStrategy

N = 10000

class RandomMapStrategy(AbstractStrategy):
    """
    The main strategy is to have a map as big as the gameboard and set each
    field to value relative to it's likelyhood of containing a ship.
    The simplest approach is chosen here, which is to have the highest value
    being the amount of all ships
    """

    def prepare(self):
        self.probability_map = [1] * (self.width * self.height)

    def get_move(self):
        #move
        max_val = max(self.probability_map)
        max_pos = [i for i, j in enumerate(self.probability_map) if j == max_val]
        pos = choice(max_pos)
        x = pos // self.width
        y = pos % self.width

        while self.get_field_info(x,y) != FIELD.UNKNOWN:
            del max_pos[pos]
            pos = choice(max_pos)


        move, field = self.evaluate(x, y)
        #update local state
        self.probability_map[pos] = 0
