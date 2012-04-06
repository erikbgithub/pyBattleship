# -*- coding: utf-8 -*-

#imports
import random
from game import *
from constants import *

#functions

def make_mem_equal():
    def inner(a,b,cache=[None]):
        last = cache[0] if cache[0] != None else a
        cache[0] = b
        return last == b if a != False else False
    return inner

