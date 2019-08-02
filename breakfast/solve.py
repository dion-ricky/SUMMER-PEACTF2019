#!/usr/bin/env python3
import re

flag = []

for i in re.findall("[01]{5}", open('enc.txt', 'r').read()):
    flag.append(chr(int(i, 2)+97))

print(''.join(flag))
