#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example

T = True
F = False
# Each day
Day = 7
Year = 2024
ReadyA = F
ReadyB = F
TestA = F
TestA_custom = False
TestB = True
TestB_custom = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    def add(a, b):
        return a + b
    def mult(a, b):
        return a * b
    ops = [add, mult]
    total = 0
    for line in data.splitlines():
        final_ans, nums = line.split(": ")
        nums = [int(x) for x in nums.split()]
        final_ans = int(final_ans)
        op_positions = len(nums) - 1
        poss_answers = [nums[0]]
        for ii in range(op_positions):
            # [OLD ANSWERS] OPERATOR num[ii+1]
            # ii = 0 TO ii = (N - 1)
            new_answers = []
            for ans in poss_answers:
                for op in ops:
                    new_answers.append(op(ans, nums[ii+1]))
            poss_answers = new_answers
        if final_ans in poss_answers:
            total += final_ans
    return str(total)


    
    pass
# part 2
def part2(data):
    def add(a, b):
        return a + b
    def mult(a, b):
        return a * b
    def concat(a, b):
        return int(str(a)+str(b))

    ops = [add, mult, concat]
    total = 0
    for line in data.splitlines():
        final_ans, nums = line.split(": ")
        nums = [int(x) for x in nums.split()]
        final_ans = int(final_ans)
        op_positions = len(nums) - 1
        poss_answers = [nums[0]]
        for ii in range(op_positions):
            # [OLD ANSWERS] OPERATOR num[ii+1]
            # ii = 0 TO ii = (N - 1)
            new_answers = []
            for ans in poss_answers:
                for op in ops:
                    new_answers.append(op(ans, nums[ii+1]))
            poss_answers = new_answers
        if final_ans in poss_answers:
            total += final_ans
    return str(total)
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