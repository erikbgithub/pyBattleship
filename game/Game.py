# -*- coding: utf-8 -*-

import os
from time import sleep
from traceback import print_exc

from distributors.RandomDistributor import RandomDistributor
from strategies.RandomStrategy import RandomStrategy

from constants import STATE, FIELD, MOVE, BOARD_SIZE, DEFAULT_SHIPS
from Board import Board

#TODO: board size, ship count
class Game:
    """TODO: description"""

    def __init__(self, distributor=RandomDistributor, strategy=RandomStrategy,
                 width=BOARD_SIZE, height=BOARD_SIZE, start_ships=DEFAULT_SHIPS):
        self.board = Board(width, height, start_ships)
        self.state = STATE.STARTING
        self.width = width
        self.height = height

        self.dist = distributor()
        self.player = strategy()
        self.moves = []

        # number of invalid moves
        self.strikes = 0
        self.destroyed = 0
        self.on_turn = False


    def prepare(self):
        self.state = STATE.STARTING
        self.board.reset()
        del self.moves[:]

        self.dist.set_ships(self.board)
        self.player.set_callbacks(self.evaluate, self.get_field_info, self.get_board_info)
        self.player.init()
        self.destroyed = 0


    def play(self, animate=False, step=False):
        # not all available ships were placed onto board
        if self.board.free_ships:
            self.state = STATE.INVALID
            return

        if animate:
            os.system("clear")

        self.state = STATE.PLAYING
        while True:
            self.on_turn = True

            if animate:
                print "\033[0;0H" # clean board and 5 additional lines
                n = self.__str__().count("\n")
                for line in range(n + 7):
                    print " " * 80

                # jump back to cursor under board
                print "\033[%d;0H" % (n + 2)

            try:
                self.player.get_move()
            except:
                self.state = STATE.INVALID
                print_exc()
                return

            if animate:
                # set cursor to line 0
                print "\033[0;0H"
                print self
                if step:
                    raw_input()
                else:
                    sleep(0.25)

            if self.destroyed == len(self.board.start_ships):
                self.state = STATE.WON
                return


    def turn_count(self):
        return len(self.moves)

    def illegal_move(self):
        if self.strikes > 5:
            self.state = STATE.INVALID
            raise Exception("Player disqualified")

        self.strikes += 1
        return MOVE.ILLEGAL, FIELD.UNKNOWN

    def evaluate(self, x, y):
        """  return Move, Field  """

        if not self.on_turn:
            return self.illegal_move()

        try:
            field = self.board.get_field(x, y)

            if (x, y) in self.moves:
                return MOVE.OLD, field

            self.moves.append((x, y))
            self.on_turn = False

            if field == FIELD.EMPTY:
                self.board.set_field(x, y, FIELD.MISS)
                return MOVE.OK, FIELD.MISS

            elif field == FIELD.SHIP:
                self.board.set_field(x, y, FIELD.HIT)

                if self.board.is_destroyed(x, y):
                    self.destroyed += 1

                    return MOVE.OK, FIELD.DESTROYED
                else:
                    return MOVE.OK, FIELD.HIT
            else: # should not happen
                return MOVE.OLD, field

        except:
            print_exc()
            return self.illegal_move()

    def get_field_info(self, x, y):
        """  can be used by strategy to get info for a field, hides information for undetected fields"""

        field = self.board.get_field(x, y)
        if field in (FIELD.HIT, FIELD.DESTROYED, FIELD.MISS):
            return field
        else:
            return FIELD.UNKNOWN

    def get_board_info(self):
        return self.width, self.height, self.board.start_ships

    def animate(self):
        os.system("clear")
        self.board.reset()

        for move in self.moves:
            self.on_turn = True
            self.evaluate(*move)
            # set cursor to line 0
            print "\033[0;0H"
            print self
            sleep(0.5)

    def get_name(self):
        return "%s vs. %s" % (self.dist.__class__.__name__, self.player.__class__.__name__)

    def get_game_info(self):
        return "Board: %sx%s | Ships: %s | Sum: %s" % (
            self.width, self.height, self.board.start_ships, sum(self.board.start_ships))

    def __str__(self):
        s = "\t%s\n\t%s" % (self.get_name(), self.get_game_info())
        s += "\n" + self.board.__str__()
        s += "\n\tturns: %s | state: %s" % (self.turn_count(), STATE.name(self.state))
        return s
