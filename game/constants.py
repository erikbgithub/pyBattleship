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


class MOVE:
    ILLEGAL = 1
    OLD = 2
    OK = 4

moves = {
        MOVE.ILLEGAL : 'illegal',
        MOVE.OLD : 'old',
        MOVE.OK : 'ok'
}

class STATE:
    STARTING = 1
    PLAYING = 2
    WON = 4
    INVALID = 8

    @staticmethod
    def name(state):
        if state == STATE.STARTING:
            return "STARTING"
        elif state == STATE.PLAYING:
            return "PLAYING"
        elif state == STATE.WON:
            return "WON"
        else:
            return "INVALID"


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
