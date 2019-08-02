#!/usr/bin/env python3

flag = []

with open('enc.txt', 'r') as _d:
    for i in _d.read().split(' '):
        flag.append(chr(int(i)))

print(''.join(flag))
