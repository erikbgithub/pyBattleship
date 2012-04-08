# -*- coding: utf-8 -*-

from random import  choice

from game.constants import DIR

from AbstractDistributor import AbstractDistributor

class RandomDistributor(AbstractDistributor):
    """
    This distributor simply puts boats on random positions.
    Thus it delivers a basic framework for ship deployment
    and a testing ground for solvers that don't use specific
    knowledge about their oponents.
    """
    
    def set_ships(self, board):
        directions = [DIR.UP, DIR.DOWN, DIR.LEFT, DIR.RIGHT]
        positions = [(x, y) for x in xrange(board.width) for y in xrange(board.height)]

        #don't try more often then each direction from each position
        max_tries = range(4 * board.width * board.height)
        for s in board.start_ships:
            for i in max_tries:
                x, y = choice(positions)
                dire = choice(directions)
                if board.add_ship(s, x, y, dire):
                    break
