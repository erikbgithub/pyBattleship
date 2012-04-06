# -*- coding: utf-8 -*-

def bits_set(mask, bin):
    """  check if all bits in mask are set in bin """
    return (bin & mask) == mask


def make_mem_equal():
    def inner(a, b, cache=[None]):
        last = cache[0] if cache[0] is not None else a
        cache[0] = b
        return last == b if a != False else False

    return inner