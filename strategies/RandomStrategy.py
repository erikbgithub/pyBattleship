# -*- coding: utf-8 -*-

from random import choice

from game.constants import MOVE

from AbstractStrategy import AbstractStrategy

class RandomStrategy(AbstractStrategy):
    def prepare(self):
        self.positions = [(x, y) for x in xrange(self.width) for y in xrange(self.height)]

    def get_move(self,state,last_result):
        """
        creates the next move. in RandomStrategy it is simply one randomly chosen field.
        """

        while True:
            x, y = choice(self.positions)
            if self.evaluate(x,y):
                self.positions.remove((x, y))
                return (x,y)
            else:
                print "eval failed for", (x,y)
