#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == None:
        sentence[0] = None
    return (len(sentence), sentence[0])
