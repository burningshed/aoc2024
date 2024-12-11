#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import numpy as np

# Each day
Day = 11
Year = 2024
ReadyA = False
ReadyB = False
TestA = False
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
    # rule 1 - 0 becomes 1
    def rule_1():
        pass
    # rule 2 - split even number of digits
    def rule_2():
        pass
    # rule 3 - multiply by 2024
    def rule_3():
        pass
    
    class Stone:
        __slots__ = ["val", "right", "left"]
        def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None
            pass
        def pick_rule(self):
            if self.val == 0:
                self.rule_1()
            elif len(str(self.val)) % 2 == 0:
                self.rule_2()
            else:
                self.rule_3() 
        def rule_3(self):
            self.val *= 2024
        def rule_1(self):
            self.val = 1
        def rule_2(self):
            str_val = str(self.val)
            midpoint = int(len(str_val) / 2)
            right_val, left_val = int(str_val[:midpoint]), int(str_val[midpoint:])
            self.insert_right(Stone(right_val))
            #self.insert_left(Stone(left_val))
            self.val = left_val
        def insert_right(self, new_right):
            new_right.right = self.right
            new_right.left = self
            if self.right != None:
                self.right.left = new_right
            self.right = new_right
        def insert_left(self, new_left):
            new_left.left = self.left
            new_left.right = self
            if self.left != None:
                self.left.right = new_left
            self.left = new_left
    def step(first_stone):
        cur_stone = first_stone
        while cur_stone != None:
            print("step")
            cur_stone.pick_rule()
            cur_stone = cur_stone.right
    a = Stone(4000) 
    step(a)
    print(a.val)
    
    

    pass
# part 2
def part2(data):
    pass
part1(puz_data)
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