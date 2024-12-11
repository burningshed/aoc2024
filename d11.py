#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import numpy as np
from functools import cache
from collections import defaultdict
import time

# Each day
Day = 11
Year = 2024
ReadyA = False
ReadyB = True
TestA = False
TestA_custom = False
TestB = False
TestB_custom = True

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    class Stone:
        __slots__ = ["val", "right", "left", "blinks"]
        def __init__(self, val, blinks=0):
            self.val = val
            self.right = None
            self.left = None
            self.blinks = blinks
            pass
        def pick_rule(self, cur_blink):
            if cur_blink != self.blinks+1:
                return False
            self.blinks += 1
            if self.val == 0:
                self.rule_1()
            elif len(str(self.val)) % 2 == 0:
                self.rule_2()
            else:
                self.rule_3() 
            return True
        def rule_3(self):
            self.val *= 2024
        def rule_1(self):
            self.val = 1
        def rule_2(self):
            str_val = str(self.val)
            midpoint = int(len(str_val) / 2)
            left_val, right_val = int(str_val[:midpoint]), int(str_val[midpoint:])
            self.insert_right(Stone(right_val, self.blinks))
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
    def step(first_stone, blinks):
        cur_stone = first_stone
        while cur_stone != None:
            cur_stone.pick_rule(blinks)
            cur_stone = cur_stone.right
            
    def print_stones(first_stone):
        cur_stone = first_stone
        print()
        while cur_stone != None:
            print(cur_stone.val, end=" ")
            cur_stone = cur_stone.right
        print()
    
    def count_stones(first_stone):
        cur_stone = first_stone
        count = 0
        while cur_stone != None:
            count += 1
            cur_stone = cur_stone.right
        return count
                
    stone_list = [int(x) for x in data.split()]
    first = Stone(stone_list[0])
    last = first
    for stone in stone_list[1:]:
        last.right = Stone(stone)
        last.right.left = last
        last = last.right
    for ii in range(26):
        step(first, ii)
    ans = count_stones(first)
    print(ans)
    return str(ans)
    
    

    pass
# part 2
def part2_old(data):
    class Stone:
        __slots__ = ["val", "right", "left", "blinks"]
        def __init__(self, val, blinks=0):
            self.val = val
            self.right = None
            self.left = None
            self.blinks = blinks
            pass
        def pick_rule(self, cur_blink):
            if cur_blink != self.blinks+1:
                return False
            self.blinks += 1
            if self.val == 0:
                self.rule_1()
            elif len(str(self.val)) % 2 == 0:
                self.rule_2()
            else:
                self.rule_3() 
            return True
        
        def rule_3(self):
            self.val *= 2024
        
        def rule_1(self):
            self.val = 1
        
        def rule_2(self):
            str_val = str(self.val)
            midpoint = int(len(str_val) / 2)
            left_val, right_val = int(str_val[:midpoint]), int(str_val[midpoint:])
            self.insert_right(Stone(right_val, self.blinks))
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
    
    def step(first_stone, blinks):
        cur_stone = first_stone
        while cur_stone != None:
            cur_stone.pick_rule(blinks)
            cur_stone = cur_stone.right
            
    def print_stones(first_stone):
        cur_stone = first_stone
        print()
        while cur_stone != None:
            print(cur_stone.val, end=" ")
            cur_stone = cur_stone.right
        print()
    
    def count_stones(first_stone):
        cur_stone = first_stone
        count = 0
        while cur_stone != None:
            count += 1
            cur_stone = cur_stone.right
        return count
                
    stone_list = [int(x) for x in data.split()]
    first = Stone(stone_list[0])
    last = first
    for stone in stone_list[1:]:
        last.right = Stone(stone)
        last.right.left = last
        last = last.right
    for ii in range(76):
        step(first, ii)
    ans = count_stones(first)
    print(ans)
    return str(ans)
    pass

def part2_old2(data):
    steps = 75
    substep_length = 1
    
    @cache
    def apply_rule(stone):
        stone_num = int(stone)
        if stone_num == 0:
            return '1'
        elif len(stone) % 2 == 0:
            midpoint = int(len(stone) / 2)
            return str(int(stone[:midpoint])) + ' ' + str(int(stone[midpoint:]))
        else:
            return str(stone_num*2024)
    @cache
    def process_stone(stone, steps=1):
        stone_str = stone
        for ii in range(steps):
            new_stones = ''
            for stone in stone_str.split():
                new_stones += ' ' + apply_rule(stone)
            stone_str = new_stones
        return stone_str
            
    initial_stones = data.split()
    substeps = int(steps / substep_length)
    remainder = steps % substep_length
    count = 0
    for stone in initial_stones:
        stone_str = stone
        for ii in range(substeps):
            print(ii)
            new_stones = ''
            for stone in stone_str.split():
                new_stones += ' ' + process_stone(stone, substep_length)
            stone_str = new_stones
        for ii in range(remainder):
            new_stones = ''
            for stone in stone_str.split():
                new_stones += ' ' + apply_rule(stone)
            stone_str = new_stones
        count += len(stone_str.split())
    return str(count)
def part2(data):
    # Trying with just tracking number of stones of each number
    stone_list = data.split()
    stone_dict = dict()
    stone_set = set(stone_list)
    steps = 75
    def apply_rule(stone):
        stone_str = str(stone)
        if stone == 0:
            return [1]
        elif len(stone_str) % 2 == 0:
            midpoint = int(len(stone_str) / 2)
            return [int(stone_str[:midpoint]), int(stone_str[midpoint:])]
        else:
            return [stone*2024]
    class Stone:
        def __init__(self, val, num=0):
            self.val = val
            self.num = num
            self.result = apply_rule(val)
    for stone in stone_set:
        stone_dict[int(stone)] = Stone(int(stone))
    for stone in stone_list:
        stone_dict[int(stone)].num += 1
    def step(old_stone_dict):
        new_stone_dict = dict()
        for stone_key in old_stone_dict:
            new_stones = old_stone_dict[stone_key].result
            for stone in new_stones:
                if stone not in new_stone_dict:
                    new_stone_dict[stone] = Stone(stone)
                new_stone_dict[stone].num += old_stone_dict[stone_key].num
        return new_stone_dict
    def count_stones(old_stone_dict):
        count = 0
        for stone_key in old_stone_dict:
            count += old_stone_dict[stone_key].num
        return count
    for _ in range(steps):
        stone_dict = step(stone_dict)
    return str(count_stones(stone_dict))


    
custom_example = [
    Example(
        "0", 
        '1', 
        '1'
        ),
    Example(
        "125 17",
        None,
        '55312'
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
    
    start = time.time()
    ansB = part2(puz_data)
    end = time.time()
    print(f"Timer: {end-start}")
    print("Answer Part B:")
    print(ansB)
    submit(ansB, part='b', day=Day, year=Year, session=token)
elif ReadyA:
    ansA = part1(puz_data)
    submit(ansA, part='a', day=Day, year=Year, session=token)