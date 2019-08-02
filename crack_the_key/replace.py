#!/usr/bin/env python3

def replace(line, dict):
    retr = line
    for i in dict:
        retr = retr.replace(i, dict[i])

    return retr

if __name__ == '__main__':
    replacement = {'I':'e', 'S':'r', 'K':'a', 'P':'n', 'L':'d', 'X':'t', 'H':'h'}
    with open('enc.txt') as _f:
        for line in _f.read().split('/n'):
            print(replace(line, replacement))
