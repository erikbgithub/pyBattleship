# -*- coding: utf-8 -*-
#imports
from constants import *

class Referee:
    def __init__(self):
        pass

    def evaluate(self, move, game):
        if game.board[move] == game.sym_empty:
            return STATE_MISS
        elif game.board[move] in [game.sym_hit, game.sym_miss]:
            return STATE_OLD

        if move == False:
            return STATE_ILLEGAL

        try:
            #test if it's a ship
            int(game.board[move])
            filtered = filter(lambda x: x not in [game.sym_empty, game.sym_hit, game.sym_miss], game.board)
            if len(filtered) <= 1:
                return STATE_WIN
            else:
                return STATE_HIT
        except BaseException, e:
            print "Exception:" + str(e)
            return STATE_ILLEGAL
