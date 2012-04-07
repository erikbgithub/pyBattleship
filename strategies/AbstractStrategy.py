# -*- coding: utf-8 -*-

class AbstractStrategy(object):
    """
    Abstract class for all strategy algorithm. They supposed to play the game and sank opponents ships.
    """

    def __init__(self, game):
        self.game = game

    def prepare(self):
        pass

    def get_move(self):
        """ Will be called  by the game, an move has to be made in this method. """
        raise NotImplementedError

    def evaluate(self, x, y):
        """ Evaluate move at desired posiition. **Has** to be called once a move.
            Coordinates are 0,0 top left based

        :param x:  x coordinate
        :param y:  y coordinate
        :return: Tuple of (Move, Field) state
        """
        return self.game.evaluate(x, y)
