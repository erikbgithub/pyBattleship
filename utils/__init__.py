# -*- coding: utf-8 -*-

def bits_set(mask, bin):
    """  check if all bits in mask are set in bin """
    return (bin & mask) == mask


def avg(seq):
    return round(float(sum(seq)) / len(seq), 2)


def median(seq):
    return sorted(seq)[len(seq) / 2]
