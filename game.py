# -*- coding: utf-8 -*-
#imports
from constants import *
from framework import *

class Game:
    
    def __init__(self, func_distrib, solver, referee, width=BOARD_SIZE,height=BOARD_SIZE, sym_empty=SYM_EMPTY, sym_hit=SYM_HIT, sym_miss=SYM_MISS, sym_unknown=SYM_UNKNOWN, start_ships=DEFAULT_SHIPS, state=STATE_START):
        self.func_distrib = func_distrib
        self.solver = solver
        self.referee = referee
        self.sym_empty = sym_empty
        self.sym_hit = sym_hit
        self.sym_miss = sym_miss
        self.sym_unknown = sym_unknown
        self.state = {'name':state,'turn':0, 'width':width,'height':height,'start_ships':start_ships,'dead_ships':[]}
        self.ship_list = [[] for s in self.state['start_ships']]
        #set the board:
        self.func_distrib(self,solver)


    def add(self,size, pos, direction, mem_ship_num=[0]):
        accepted = [pos]
        for i in map(lambda x: x+1, range(size-1)):
            inner_pos = pos
            if direction == DIR_UP:
                inner_pos -= i*self.state['width']
            elif direction == DIR_DOWN:
                inner_pos += i*self.state['width']
            elif direction == DIR_LEFT:
                inner_pos -= i
            elif direction == DIR_RIGHT:
                inner_pos += i
            else:
                pass #should never occur
            
            #check if ship can be added
            if(inner_pos < 0 or inner_pos >= len(self.board) or self.board[inner_pos] != SYM_EMPTY):
                return False
            else:
                accepted += [inner_pos]

        #check for ships crossing boardboundaries
        cols = [self.get_col(pos) for pos in accepted]
        rows = [self.get_row(pos) for pos in accepted]
        if(direction in [DIR_LEFT,DIR_RIGHT] and not reduce(make_mem_equal(),cols)):
            return False
        elif(direction in [DIR_UP,DIR_DOWN] and not reduce(make_mem_equal(),rows)):
            return False

        #ship has a legal position, so add to board
        mem_ship_num[0] += 1
        for pos in accepted:
            self.board[pos] = str(mem_ship_num[0]).zfill(2)
        return True

    def next_move(self):
        '''create and evaluate next move'''
        #if we are in an illegal state, we shouldn't
        #create new moves
        if self.state['name'] == STATE_ILLEGAL:
            return False
        #get a move and evaluate it
        move = self.solver.get_move(self.state)
        self.state['name'] = self.referee.evaluate(move,self)
        #print 'move:'+str(move)+',state:'+str(self.state)
        #react according to judgement
        if self.state['name'] in [STATE_ILLEGAL,STATE_UNCERTAIN]:
            return False
        elif self.state['name'] == STATE_OLD:
            #this means the generated move was on the same spot a HIT or MISS
            #was already evaluated before
            return True
        elif self.state['name'] in [STATE_EMPTY,STATE_HIT,STATE_DESTROYED,STATE_MISS]:
            self.board[move] = TRANSLATE_STATE_SYM[self.state['name']](self)
            self.state['turn'] += 1
            return True
        elif self.state['name'] == STATE_DESTROYED:
            ship = int(self.board[move])
            self.state['dead_ships'] += ship
            self.board[move] = TRANSLATE_STATE_SYM[self.state['name']](self)
            self.state['turn'] += 1
            return True
        elif self.state['name'] == STATE_WIN:
            self.board[move] = TRANSLATE_STATE_SYM[self.state['name']](self)
            self.state['turn'] += 1
            return False
        else:
            self.state['name'] = STATE_UNCERTAIN
            return False

    def solve(self):
        for i in range(len(self.board)):
            if not self.next_move(): break

    def get_col(self,pos):
        return pos // self.state['width']

    def get_row(self,pos):
        return pos % self.state['width']

    def print_board(self):
        width = self.state['width']
        ranges = [(y*width,(y+1)*width) for y in range(width)]
        return '\n'.join([' '.join(self.board[s1:s2]) for s1,s2 in ranges])

    def __str__(self):
        txt  = 'state : '+str(self.state)+'\n'
        txt += 'board :\n'
        txt += self.print_board()
        return txt
