#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
from AoCHelpers import coord
import numpy as np
T = True
F = False
# Each day
Day = 8
Year = 2024
ReadyA = F
ReadyB = T
TestA = F
TestA_custom = F
TestB = T
TestB_custom = T

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    map = []
    antennas = dict()
    yy = 0
    for line in data.splitlines():
        xx = 0
        row = [x for x in line]
        map.append(row)
        for node in row:
            if node == '.':
                xx += 1
                continue
            antennas[node] = antennas.get(node, []) + [coord(xx, yy)]
            xx += 1
        yy += 1
    boundries = [coord(0, 0), coord(yy-1, xx-1)]
        
    def find_antipodes(first, other):
        direction = first - other
        a = first + direction
        b = other - direction
        #print(a,b)
        valid = []
        if not (a <= boundries[0] or a >= boundries[1]):
            valid.append(a)
        if not (b <= boundries[0] or b >= boundries[1]):
            valid.append(b)
        #print(valid)
        return valid
    targets = set()
    for key in antennas:
        for ii in range(len(antennas[key])-1):
            for spot in antennas[key][ii+1:]:
                targets.update(find_antipodes(antennas[key][ii], spot))
            
    print(targets)
    print(antennas.keys())
    print(f"Number of Unique Spots: {len(targets)}")    
    map2 = np.array(map)
    print(map2)
    for target in targets:
        map2[target.y][target.x] = '#'
    print(map2)
    return(str(len(targets)))


# part 2
def part2(data):
    map = []
    antennas = dict()
    yy = 0
    for line in data.splitlines():
        xx = 0
        row = [x for x in line]
        map.append(row)
        for node in row:
            if node == '.':
                xx += 1
                continue
            antennas[node] = antennas.get(node, []) + [coord(xx, yy)]
            xx += 1
        yy += 1
    boundries = [coord(0, 0), coord(yy-1, xx-1)]
    def find_antinode(first, direction):
        a = first + direction
        if a <= boundries[0] or a >= boundries[1]:
            return []
        return find_antinode(a, direction) + [a]
    def find_antinodes(first, other):
        direction = first - other
        antinode_list_a = find_antinode(first, direction) + [first]
        antinode_list_b = find_antinode(other, coord(0,0)-direction) + [other]
        return antinode_list_a + antinode_list_b
    def find_antipodes(first, other):
        direction = first - other
        a = first + direction
        b = other - direction
        #print(a,b)
        valid = []
        if not (a <= boundries[0] or a >= boundries[1]):
            valid.append(a)
        if not (b <= boundries[0] or b >= boundries[1]):
            valid.append(b)
        #print(valid)
        return valid
    targets = set()
    for key in antennas:
        for ii in range(len(antennas[key])-1):
            for spot in antennas[key][ii+1:]:
                targets.update(find_antinodes(antennas[key][ii], spot))
            
    print(targets)
    print(antennas.keys())
    print(f"Number of Unique Spots: {len(targets)}")    
    """
    map2 = np.array(map)
    print(map2)
    for target in targets:
        map2[target.y][target.x] = '#'
    print(map2)"""
    return(str(len(targets)))
    pass

custom_example = [
    Example(
        """..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........""", 
        '2', 
        None
        ),
    Example(
        """..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
..........""",
        '4',
        None
        ),
    
    Example(
        """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........""",
        None,
        '9'
        )

    ]

if TestA:
    tester(part1, 'a', puzzle)

if TestA_custom:
    tester(part1, 'a', puzzle, custom_example)
    
if TestB:
    tester(part2, 'b', puzzle)
    
if TestB_custom:
    tester(part2, 'b', puzzle, custom_example)        
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    submit(ansB, part='b', day=Day, year=Year, session=token)
elif ReadyA:
    ansA = part1(puz_data)
    submit(ansA, part='a', day=Day, year=Year, session=token)