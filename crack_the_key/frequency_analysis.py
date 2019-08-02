#!/usr/bin/env python3

def max(dict):
    max = 0
    retr = {}
    for i in dict:
        if dict[i] > max:
            max = dict[i]

    for i in dict:
        if dict[i] == max:
            retr[i] = dict[i]

    return retr

def single():
    data = {}
    with open('enc.txt') as _f:
        for line in _f.read().split('/n'):
            for char in line:
                if char in data:
                    data[char] += 1
                else:
                    data[char] = 1

    return data

def ngram(n=2):
    data = {}
    with open('enc.txt') as _f:
        for line in _f.read().split('/n'):
            for i in range(0, len(line), n):
                ngram = line[i:i+n]
                if ngram in data:
                    data[ngram] += 1
                else:
                    data[ngram] = 1
    return data

def bigram():
    return ngram(2)

def trigram():
    return ngram(3)

if __name__ == '__main__':
    print('Single:', max(single()))
    print('Bigram:', max(bigram()))
    print('Trigram:', max(trigram()))
