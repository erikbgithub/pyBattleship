# -*- coding: utf-8 -*-
#imports
from constants import *
from random import *

class Random_Solver:
    def __init__(self, sym_empty=SYM_EMPTY, sym_hit=SYM_HIT, sym_miss=SYM_MISS, sym_unknown=SYM_UNKNOWN):
        self.sym_empty = sym_empty
        self.sym_hit = sym_hit
        self.sym_miss = sym_miss
        self.sym_unknown = sym_unknown
        self.board = []

    def get_move(self, state):
        name = state['name']
        if name == STATE_START:
            self.board = [self.sym_unknown for i in range(state['width'] * state['height'])]
        elif name in [STATE_HIT, STATE_DESTROYED, STATE_MISS]:
            self.board[self.last_move] = TRANSLATE_STATE_SYM[name](self)

        moves = range(len(self.board))
        shuffle(moves)
        shuffle(moves)
        while len(moves) > 0:
            move = moves.pop()
            if self.board[move] in [self.sym_hit, self.sym_miss]: continue
            self.last_move = move
            return move
        return False
