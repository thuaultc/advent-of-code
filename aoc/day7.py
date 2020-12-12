#! /usr/bin/env python3

def _parse(f):
    lines = [l for l in [x.strip() for x in f.readlines()]]
    input = {}
    for l in lines:
        bag, contents = l.split('contain')
        bag_name = bag.split(' bags')[0].replace(' ', '-')
        input[bag_name] = {}

        if 'no other bags' in contents:
            continue

        contents_array = contents.split(' ')[1:]
        del contents_array[3::4]

        for i in range(len(contents_array) // 3):
            input[bag_name][f'{contents_array[i*3+1]}-{contents_array[i*3+2]}'] = int(contents_array[i*3])
    return input

def _check_bags(bag, input):
    bags = []
    for k, v in input.items():
        if bag in v.keys():
            bags.append(k)

    return bags

def _star1(input):
    total_bags = []
    bags = ['shiny-gold']
    while bags:
        contained_bags = []
        for bag in bags:
            contained_bags.extend(_check_bags(bag, input))
        total_bags.extend(contained_bags)
        bags = contained_bags
    return len(list(set(total_bags)))

def _count_bags(bag, input):
    count = 1
    for k, v in input[bag].items():
        count += v * _count_bags(k, input)

    return count

def _star2(input):
    return _count_bags('shiny-gold', input) - 1

def run(f):
    input = _parse(f)
    return (_star1(input), _star2(input))