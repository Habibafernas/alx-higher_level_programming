#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    tuple_c = tuple_a + (0, 0)
    tuple_d = tuple_b + (0, 0)
    new = tuple_c[0] + tuple_d[0], tuple_c[1] + tuple_d[1]
    return new
