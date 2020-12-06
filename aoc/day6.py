#! /usr/bin/env python3

def _parse(f):
    lines = [l for l in [x.strip() for x in f.readlines()]]
    group = []
    input = []
    for l in lines:
        if l == '':
            input.append(group)
            group = []
            continue
        group.append(l)
    input.append(group)

    return input

def _star1(input):
    count = 0
    for group in input:
        answers = ''
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers += answer
        count += len(answers)
    return count

def _star2(input):
    count = 0
    for group in input:
        persons = len(group)
        answers = {}
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers[answer] = 1
                else:
                    answers[answer] += 1
        for answer, c in answers.items():
            if c == persons:
                count += 1
    return count

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))