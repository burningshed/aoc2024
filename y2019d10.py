#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import numpy as np

# Each day
Day = 10
Year = 2019
ReadyA = False
ReadyB = False
TestA = True
TestA_custom = False
TestB = False
TestB_custom = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    map = []
    for line in data.splitlines():
        map.append([x for x in line.split()])
    print(np.array(map))
    pass
# part 2
def part2(data):
    pass

custom_example = [
    Example(
        "example_input", 
        'answer_a', 
        'answer_b'
        ),
    Example(
        "example 2",
        'a',
        'b'
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