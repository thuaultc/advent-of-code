#! /usr/bin/env python3

import importlib
import os
import sys

def run(day):
    filepath = os.path.join(os.path.dirname(__file__), f'input/{day}.txt')
    with open(filepath) as f:
        mod = importlib.import_module(f'aoc.{day}')
        star1, star2 = mod.run(f)

        print(f'⭐ {star1}')
        print(f'⭐⭐ {star2}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py day")
        sys.exit(1)

    day = f'day{sys.argv[1]}'

    run(day)