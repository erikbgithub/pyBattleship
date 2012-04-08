# -*- coding: utf-8 -*-

from time import time

from utils import avg, median

from constants import STATE

GAME_CT = 1000

class Statistics:
    def __init__(self, game):
        self.game = game
        self.results = []

    def spawn(self, n=GAME_CT):
        # Fallback on import error or single core
        try:
            from multiprocessing import Process, Manager, cpu_count
        except ImportError:
            return self.run(n)

        # For low n multiprocessing does not gain much speed up
        if cpu_count() <= 1 or n < 500:
            return self.run(n)

        m = Manager()
        self.results = m.list()
        procs = []
        load = [n // cpu_count()] * cpu_count()

        # add the rest from division to last cpu
        load[-1] += n % cpu_count()

        for count in load:
            proc = Process(target=self.run, args=(count,))
            proc.start()
            procs.append(proc)

        [p.join() for p in procs]

    def run(self, n=GAME_CT):
        for i in range(n):
            t = time()
            self.game.prepare()
            self.game.play()

            self.results.append((self.game.state, self.game.turn_count(), (time() - t) * 1000))


    def __str__(self):
        s = "%s\n%s\n\nPlays: %s" % (self.game.get_name(), self.game.get_game_info(), len(self.results))

        data = zip(*self.results)

        invalid = filter(lambda x: x == STATE.INVALID, data[0])

        s += " | Invalid: %s" % len(invalid)

        s += "\n\tTurns\tTime"

        for name, f in (("Minimum", min), ("Avg.", avg), ("Median", median), ("Maximum", max), ("Total", sum)):
            s += "\n%s\t%s\t%.2f" % (name, f(data[1]), f(data[2]))

        return s