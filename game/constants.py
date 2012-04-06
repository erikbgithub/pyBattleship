# -*- coding: utf-8 -*-
BOARD_SIZE = 10 #both width end height, default=squared board
DEFAULT_SHIPS = [5, 4, 3, 3, 2]

# all constants can be used as bit mask, could be usefull sometimes

class FIELD:
    EMPTY = 1
    SHIP = 2
    MISS = 4
    HIT = 8
    DESTROYED = 16
    UNKNOWN = 32


class STATE:
    START = 1
    ILLEGAL = 2
    UNCERTAIN = 4
    OLD = 8
    WIN = 16

    #todo: print state


class DIR:
    #directions
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8


symbols = {
    FIELD.EMPTY: '.',
    FIELD.SHIP: "+",
    FIELD.MISS: '~',
    FIELD.HIT: '*',
    FIELD.DESTROYED: "*",
    FIELD.UNKNOWN: '?'
}