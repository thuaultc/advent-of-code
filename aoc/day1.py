#! /usr/bin/env python3

def _parse(f):
    input = [x.strip() for x in f.readlines()]
    return input

def _star1(input):
    for i in input:
        for j in input:
            sum = int(i) + int(j)
            if (sum) == 2020:
                return int(i) * int(j)

def _star2(input):
    for i in input:
        for j in input:
            for k in input:
                sum = int(i) + int(j) + int(k)
                if (sum) == 2020:
                    return int(i) * int(j) * int(k)

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))