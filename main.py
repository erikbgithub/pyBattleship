#!/usr/bin/env python2
# -*- coding: utf-8 -*-

VERSION = "0.2"

import argparse
from time import time
from numpy import zeros
import matplotlib.pyplot as plt

import distributors
import strategies

from game.constants import DEFAULT_SHIPS, BOARD_SIZE
from game.Game import Game
from game.Statistics import Statistics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python battleship simulator v%s" % VERSION)
    parser.add_argument('count', metavar="N", type=int, nargs="?", default=1000,
        help="count of games to simulate")
    parser.add_argument('ships', metavar="S", type=int, nargs="*", default=DEFAULT_SHIPS,
        help='list of ship lenghts')

    parser.add_argument('--width', metavar="WIDTH", type=int, default=BOARD_SIZE,
        help="board width")
    parser.add_argument('--height', metavar="HEIGHT", type=int, default=BOARD_SIZE,
        help="board height")

    parser.add_argument('-d', '--distributor', choices=distributors.all, default=distributors.all[0],
        help='Strategy to set ships on the board')
    parser.add_argument('-s', '--strategy', choices=strategies.all, default=strategies.all[0],
        help='Strategy to shoot ships')
    parser.add_argument('--print-game', default=False, action='store_true',
        help='Play one Game and print the board')
    parser.add_argument('--no-multi-process', default=False, action='store_true',
        help='Disable multiprocessing on all cores')

    parser.add_argument('--version', action='version', version='%%(prog)s v%s' % VERSION)

    args = parser.parse_args()

    dist = __import__("distributors.%s" % args.distributor, fromlist=[args.distributor])
    dist = getattr(dist, args.distributor)

    strategy = __import__("strategies.%s" % args.strategy, fromlist=[args.strategy])
    strategy = getattr(strategy, args.strategy)

    g = Game(dist, strategy, args.width, args.height, args.ships)

    if args.print_game:
        g.prepare()
        g.play()
    else:
        s = Statistics(g)
        t = time()

        if not args.no_multi_process:
            s.spawn(args.count)
        else:
            s.run(args.count)

        blubb = zeros(101)
        for x in s.results: blubb[x[1]] += 1
        plt.plot(blubb)
        plt.show()
        print s

        print
        print "Testing took %.2f seconds" % (time() - t)
