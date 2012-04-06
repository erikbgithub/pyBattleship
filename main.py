#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse

from game.Game import Game

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python battleship simulator")
    parser.parse_args()

    g = Game()
    g.prepare()
    print g
    print

    g.play()
    print g