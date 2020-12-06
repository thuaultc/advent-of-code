#! /usr/bin/env python3

def _parse(f):
    input = [x.strip() for x in f.readlines()]
    return input

def _slope(input, right, down):
    count = 0
    for idx, l in enumerate(input[::down][1:]):
        if l[((idx + 1) * right) % len(input[0])] == '#':
            count += 1
    return count

def _star1(input):
    count = _slope(input, 3, 1)
    return count

def _star2(input):
    count = (_slope(input, 1, 1) * _slope(input, 3, 1) *
            _slope(input, 5, 1) * _slope(input, 7, 1) *
            _slope(input, 1, 2))
    return count

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))