# -*- coding: utf-8 -*-

from random import choice
from game.constants import MOVE, FIELD, symbols, moves
from AbstractStrategy import AbstractStrategy
from operator import __add__
from pylab import pcolor, get_cmap, matrix

def make_line(width,maximum):
    return [min(i,width+1-i,maximum) for i in range(1,width+1)]

def make_rows(width,height,ship_size):
    return matrix([make_line(width,ship_size) for i in range(height)])

def make_map(width,height,ship_size):
    return make_rows(width,height,ship_size) + make_rows(height,width,ship_size).transpose()

def dists(pos,length):
    return [abs(pos-i) for i in range(length)]

def upd_miss_row(m,x,y):
    m[y] = map(min,list(m[y].flat),dists(x,m.shape[0]))
    return m

def upd_miss_col(m,x,y):
    return upd_miss_row(m.transpose(),y,x).transpose()

def upd_miss(m,x,y):
    return upd_miss_col(upd_miss_row(m,x,y),x,y)

def upd_hit(m,x,y):
    m[y,x] = 0
    return m

def upd_misses(ms,x,y):
    return [upd_miss(m,x,y) for m in ms]

def upd_hits(ms,x,y):
    return [upd_hit(m,x,y) for m in ms]

def max_poses(width,height,avg):
    maxval = max(avg.flat)
    return [(j,i) for i in range(width) for j in range(height) if avg[i,j] == maxval]


class SimpleProbStrategy(AbstractStrategy):
    """
    the idea is to calculate probabilities according to given information
    (known hits and misses) and the believe state of each ship possibly
    being everywhere as long as the position is not definitive.
    """

    def prepare(self):
        self.prob_maps = [make_map(self.width,self.height,s) for s in self.ships]
        self.average()
        self.shots = []

    def average(self):
        """
        average up all maps
        """
        self.avg = reduce(__add__,[p*1.0/len(self.ships) for p in self.prob_maps])
        return self.avg

    def get_move(self):
        pos = choice(max_poses(self.width,self.height,self.avg))
        move, field = apply(self.evaluate,pos)
        self.shots = list(set(self.shots+[pos]))

        if field == FIELD.MISS:
            self.prob_maps = upd_misses(self.prob_maps,pos[0],pos[1])
        elif field in [FIELD.HIT,FIELD.DESTROYED]:
            self.prob_maps = upd_hits(self.prob_maps,pos[0],pos[1])
        else:
            raise Exception("neither HIT nor MISS but "+symbols[field])
        self.average()


    def __init_prob_map(width,height,L):
        if type(L).__name__ == "list":
            _init = SimpleProbStrategy.__init_prob_map
            return reduce(__add__,[_init(width,height,l) for l in L])
        else:
            my_x = arange(1,width+1)
            my_y = arange(1,height+1)
            my_rows = matrix([minimum(L,minimum((width+1)-my_x, my_x))] * width)
            my_cols = matrix([minimum(L,minimum((height+1)-my_y,my_y))] * height).transpose()
            return my_rows + my_cols

    def __calc_prior(N,L):
        my_map = SimpleProbStrategy.__init_prob_map(N,L)
        calc_prior = my_map / (1.0 * psum(my_map))
        return calc_prior

    def __draw_diagram(W,cmap=get_cmap("OrRd")):
        pcolor(array,W,cmap=cmap)
        colorbar()
        show()
