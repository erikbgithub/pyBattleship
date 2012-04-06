# -*- coding: utf-8 -*-
#imports
from constants import *
from game import *
from solvers import *
from distributors import *
from referee import *
from gamelist import *
#
GAME_CT = 100000
#main
all_turns = []
solver = Random_Solver()
referee = Referee()

games = [Game(random_distrib,solver,referee) for i in range(GAME_CT)]
all_turns = [g.solve() or g.state['turn'] for g in games]
summed_up = sum(all_turns)

print "length:"+str(len(all_turns))
#print "Ausschnitt:"+str(all_turns[(GAME_CT/2):(GAME_CT/2)+100])
print "mean:"+str(float(summed_up)/float(GAME_CT))
