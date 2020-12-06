#! /usr/bin/env python3

def _parse(f):
    input = [l.split(' ') for l in [x.strip() for x in f.readlines()]]
    return input

def _star1(input):
    count = 0
    for i in input:
        min, max = i[0].split('-')
        char = i[1][0]
        password = i[2]
        if int(min) <= password.count(char) <= int(max):
            count += 1
    return count

def _star2(input):
    count = 0
    for i in input:
        pos_a, pos_b = i[0].split('-')
        char = i[1][0]
        password = i[2]
        char_a = password[int(pos_a) - 1]
        char_b = password[int(pos_b) - 1]
        if char in [char_a, char_b]:
            if char_a != char_b:
                count += 1
    return count

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))