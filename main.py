#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse

from game.Game import Game
from game.Statistics import Statistics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python battleship simulator")
    parser.parse_args()

    g = Game()
    s = Statistics(g)

    s.run(100)

    print s