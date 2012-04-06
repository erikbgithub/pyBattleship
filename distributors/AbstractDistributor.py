# -*- coding: utf-8 -*-

class AbstractDistributor(object):
    """
    Abstract class for all distribution algorithm, classes that set up the game fields with their ships.
    """

    def set_ships(self, board):
        """ All ships has to be set on the board.
        use board.add_ship for this purpose

        :param board: board instance
        """
        raise NotImplementedError