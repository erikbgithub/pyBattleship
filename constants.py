# -*- coding: utf-8 -*-
BOARD_SIZE = 10 #both width end height, default=squared board
DEFAULT_SHIPS = [5,4,3,3,2]

#symbols
SYM_EMPTY = ' .'
SYM_HIT = ' *'
SYM_MISS = ' ~'
SYM_UNKNOWN = ' ='

#states
STATE_START = 'STATE_START'
STATE_ILLEGAL = 'STATE_ILLEGAL'
STATE_UNCERTAIN = 'STATE_UNCERTAIN'
STATE_OLD = 'STATE_OLD'
STATE_EMPTY = 'STATE_EMPTY'
STATE_HIT = 'STATE_HIT'
STATE_DESTROYED = 'STATE_DESTROYED'
STATE_MISS = 'STATE_MISS'
STATE_WIN = 'STATE_WIN'

#directions
DIR_UP = 'DIR_UP'
DIR_DOWN = 'DIR_DOWN'
DIR_LEFT = 'DIR_LEFT'
DIR_RIGHT = 'DIR_RIGHT'

#translations
TRANSLATE_STATE_SYM = {
    STATE_EMPTY : lambda game: game.sym_empty,
    STATE_HIT : lambda game: game.sym_hit,
    STATE_WIN : lambda game: game.sym_hit,
    STATE_DESTROYED : lambda game: game.sym_hit,
    STATE_MISS : lambda game: game.sym_miss
}
