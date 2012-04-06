# -*- coding: utf-8 -*-

from copy import copy
from operator import add, sub

from constants import BOARD_SIZE, DEFAULT_SHIPS, FIELD, DIR, symbols

class Board:
    """
    Represents a single board, has to be filled by distributor and then played by strategy.
    """

    def __init__(self, width=BOARD_SIZE, height=BOARD_SIZE, start_ships=DEFAULT_SHIPS):
        self.turn = 0
        self.width = width
        self.height = height

        self.board = []
        self.start_ships = copy(start_ships)

    def reset(self):
        """ reset and init the game field """

        self.free_ships = copy(self.start_ships)

        # one dimensional array for whole board
        # pos = row * width + column
        self.field = [FIELD.EMPTY] * (self.width * self.height)

        # maps ship id to positions
        self.ships = {}

    def add_ship(self, ship, x, y, dir):
        if ship not in self.free_ships:
            return False

        op = add if dir in (DIR.RIGHT, DIR.DOWN) else sub

        # vertical
        if dir in (DIR.RIGHT, DIR.LEFT):
            # check if ship fits onto board
            if not(0 <= x < self.width > op(x, ship) >= 0):
                return False

            pos = [op(self.width * y + x, i) for i in range(ship)]

        # horizontal
        else:
            if not(0 <= y < self.height > op(y, ship) >= 0):
                return False

            pos = [self.width * op(y, i) + x for i in range(ship)]

        # check if crossing other ships
        if any(True for p in pos if self.field[p] != FIELD.EMPTY):
            return False

        # ship has a legal position, so add to board
        for p in pos:
            self.field[p] = FIELD.SHIP

        self.ships[len(self.ships)] = pos
        self.free_ships.remove(ship)

        return True

    def is_destroyed(self, x, y):
        pos = y * self.width + x

        # TODO optimize
        for ship in self.ships.itervalues():
            if pos in ship:
                if all(True for p in ship if p == FIELD.HIT):
                    for p in ship:
                        self.field[p] = FIELD.DESTROYED
                    return True

        return False

    def get_field(self, x, y):
        return self.field[y * self.width + x]

    def set_field(self, x, y, state):
        self.field[y * self.width + x] = state

    def get_board(self):
        return self.field

    def get_col(self, pos):
        return pos // self.width

    def get_row(self, pos):
        return pos % self.width

    def print_board(self):
        s = "-" * (self.width * 2 + 1) + "\n"
        s += "\n".join("|%s|" % " ".join(symbols[p] for p in self.field[row * self.width: (row + 1) * self.width])
        for row in xrange(self.height))
        s += "\n" + "-" * (self.width * 2 + 1)

        return s

    def __str__(self):
        return self.print_board()

if __name__ == "__main__":
    b = Board()
    b.reset()

    print b

    b.add_ship(3, 5, 5, DIR.DOWN)
    b.add_ship(3, 9, 0, DIR.DOWN)
    b.add_ship(5, 0, 0, DIR.RIGHT)
    b.add_ship(2, 9, 9, DIR.RIGHT)
    b.add_ship(2, 9, 9, DIR.LEFT)

    print b