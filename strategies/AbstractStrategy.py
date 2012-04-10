# -*- coding: utf-8 -*-

class AbstractStrategy(object):
    """
    Abstract class for all strategy algorithm. They supposed to play the game and sank opponents ships.
    """

    def __init__(self):
        self.width = self.height = self.ships = None

    def set_callbacks(self, ev, f, b):
        self.evaluate = ev
        self.get_field_info = f
        self.get_board_info = b

    def init(self):
        self.width, self.height, self.ships = self.get_board_info()
        self.prepare()

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

    def get_field_info(self, x, y):
        """ Retrieves information about field state at desired position

        :return: :class:`Field`
        """

    def get_board_info(self):
        """ Gets board information

        :return: (width, height, start_ships)
        """