# -*- coding: utf-8 -*-

from traceback import print_exc

from distributors.RandomDistributor import RandomDistributor
from strategies.RandomStrategy import RandomStrategy

from constants import FIELD, MOVE, BOARD_SIZE, DEFAULT_SHIPS
from Board import Board

#TODO: board size, ship count
class Game:
    def __init__(self, distributor=RandomDistributor, strategy=RandomStrategy,
                 width=BOARD_SIZE, height=BOARD_SIZE, start_ships=DEFAULT_SHIPS):
        self.board = Board(width, height, start_ships)
        self.width = width
        self.height = height

        self.dist = distributor()
        self.player = strategy(self)
        self.moves = []

        # number of invalid moves
        self.strikes = 0
        self.destroyed = 0
        self.on_turn = False


    def prepare(self):
        self.board.reset()
        del self.moves[:]

        self.dist.set_ships(self.board)
        self.player.start()
        self.destroyed = 0


    def play(self):
        while True:
            self.on_turn = True
            self.player.get_move()

            if self.destroyed == len(self.board.ships):
                return


    def turn_count(self):
        return len(self.moves)

    def illegal_move(self):
        if self.strikes > 5:
            raise Exception("Player disqualified")

        self.strikes += 1
        return MOVE.ILLEGAL, FIELD.UNKNOWN

    def evaluate(self, x, y):
        """  return Mpve, Field  """

        if not self.on_turn:
            return self.illegal_move()

        try:
            field = self.board.get_field(x, y)

            if (x, y) in self.moves:
                return MOVE.OLD, field

            self.moves.append((x, y))

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

        except BaseException, e:
            print_exc()
            return self.illegal_move()


    def __str__(self):
        s = "\t%s vs. %s" % (self.dist.__class__.__name__, self.player.__class__.__name__)
        s += "\n" + self.board.__str__()
        s += "\n\tturns: %s" % self.turn_count()
        return s