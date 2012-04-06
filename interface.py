# -*- coding: utf-8 -*-
#imports
from constants import *
from game import *
from distributors import *
from solvers import *
from referee import *

#main
game = Game(random_distrib,Random_Solver(),Referee())
print game
game.solve()
print game
