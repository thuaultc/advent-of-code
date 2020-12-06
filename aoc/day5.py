#! /usr/bin/env python3

def _parse(f):
    input = [x.strip() for x in f.readlines()]
    return input

def _split(arr):
    a = arr[0:len(arr)//2]
    b = arr[len(arr)//2:]
    return (a,b)

def _get_id(ticket):
    row = [*range(128)]
    col = [*range(8)]
    for i in range(7):
        if ticket[i] == "F":
            row, _ = _split(row)
        else:
            _, row = _split(row)
    for i in range(3):
        if ticket[i+7] == "L":
            col, _ = _split(col)
        else:
            _, col = _split(col)
    return row[0] * 8 + col[0]

def _star1(input):
    return max(list(map(_get_id, input)))

def _star2(input):
    seats = sorted(list(map(_get_id, input)))
    first, last = min(seats), max(seats)
    
    return list(set(range(first, last + 1)) - set(seats))[0]

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))