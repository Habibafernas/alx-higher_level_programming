#!/usr/bin/python3
def multiple_returns(sentence):
    new = ()
    if len(sentence) == 0:
        new = 0, "None"
    l = len(sentence)
    f = sentence[0]
    new = l, f
    return (new)
