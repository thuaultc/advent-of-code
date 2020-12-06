#! /usr/bin/env python3

def _parse(f):
    lines = [l for l in [x.strip() for x in f.readlines()]]
    passport = {}
    input = []
    for l in lines:
        if l == '':
            input.append(passport)
            passport = {}
            continue
        for i in l.split():
            k, v = i.split(':')
            passport[k] = v
    input.append(passport)

    return input

def _star1(input):
    count = 0
    for i in input:
        i.pop('cid', None)
        if len(i) == 7:
            count += 1
    return count

def _star2(input):
    count = 0
    for i in input:
        i.pop('cid', None)
        if len(i) != 7:
            continue
        if not 1920 <= int(i['byr']) <= 2002:
            continue
        if not 2010 <= int(i['iyr']) <= 2020:
            continue
        if not 2020 <= int(i['eyr']) <= 2030:
            continue
        if 'cm' in i['hgt']:
            if not 150 <= int(i['hgt'].split('cm')[0]) <= 193:
                continue
        elif 'in' in i['hgt']:
            if not 59 <= int(i['hgt'].split('in')[0]) <= 76:
                continue
        else:
            continue
        if len(i['hcl']) == 7 and i['hcl'][0] == '#':
            for idx in range(6):
                if i['hcl'][idx + 1] not in '0123456789abcdef':
                    continue
        else:
            continue
        if i['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if len(i['pid']) != 9:
            continue
        count += 1
    return count

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))