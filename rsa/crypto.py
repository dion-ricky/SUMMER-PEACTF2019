#!/usr/bin/env python3
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random = Random.new().read
key = RSA.generate(1024, random)

publickey = key.publickey()

encrypted = publickey.encrypt(32, 'encrypt this message')

print('encrypted message:', encrypted)
f = open('enc.txt', 'w+')
f.write(str(encrypted))
f.close()
