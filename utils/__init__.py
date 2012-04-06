# -*- coding: utf-8 -*-

def make_mem_equal():
    def inner(a, b, cache=[None]):
        last = cache[0] if cache[0] != None else a
        cache[0] = b
        return last == b if a != False else False

    return inner