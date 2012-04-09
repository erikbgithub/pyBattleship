# -*- coding: utf-8 -*-

class AbstractStrategy(object):
    """
    Abstract class for all strategy algorithm. They supposed to play the game and sank opponents ships.
    """

    def __init__(self, width, height, evaluate):
        self.width = width
        self.height = height
        self.evaluate = evaluate

    def prepare(self):
        pass

    def get_move(self, state, last_result):
        """ Will be called  by the game, an move has to be made in this method. 
        :param state: the current Game state
        :param last_result: a tuple of a move-evaluation and a field-type, 
                            both of the field last shot at;
                            allows to check what happened last move
        """
        raise NotImplementedError

    def evaluate(self, x, y):
        """ Evaluate move at desired posiition. **Has** to be called once a move.
            Coordinates are 0,0 top left based

        :param x:  x coordinate
        :param y:  y coordinate
        :return: boolean
        """
        return self.evaluate(x, y)
