# -*- coding: utf-8 -*-
#imports
from constants import *
from random import *

#distributors
def random_distrib(game, solver):
    game.board = [SYM_EMPTY for i in range(game.state['width']*game.state['height'])]
    directions = [DIR_UP,DIR_DOWN,DIR_LEFT,DIR_RIGHT]
    last_pos = len(game.board)-1
    #don't try more often then each direction from each position
    max_tries = range(4*game.state['width']*game.state['height'])
    for s in game.state['start_ships']:
        for i in max_tries:
            pos = randint(0,last_pos)
            dire = choice(directions)
            if game.add(s,pos,dire):
                break


#helpers
