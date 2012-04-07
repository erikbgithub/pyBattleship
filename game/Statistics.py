# -*- coding: utf-8 -*-

from time import time

from utils import avg, mean

from constants import STATE

GAME_CT = 1000

class Statistics:
    def __init__(self, game):
        self.game = game

        self.results = []

    def run(self, n=GAME_CT):
        for i in range(n):
            t = time()
            self.game.prepare()
            self.game.play()

            self.results.append((self.game.state, self.game.turn_count(), (time() - t) * 1000))


    def __str__(self):
        s = "%s\nPlays: %s" % (self.game.get_name(), len(self.results))

        data = zip(*self.results)

        invalid = filter(lambda x: x == STATE.INVALID, data[0])

        s += " | Invalid: %s" % len(invalid)

        s += "\n\tTurns\tTime"

        for name, f in (("Minimum", min), ("Avg.", avg), ("Mean", mean), ("Maximum", max), ("Total", sum)):
            s += "\n%s\t%s\t%.2f" % (name, f(data[1]), f(data[2]))

        return s