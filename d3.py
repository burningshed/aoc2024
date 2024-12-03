#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from tester import tester, Example

# Each day
Day = 3
Year = 2024
ReadyA = False
ReadyB = False
TestA = False
TestB = True

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    total = 0
    for part in data.split("mul")[1:]:
        this_tot = 1
        if part[0] == '(':
            working_string = part[1:].split(')')[0].split(',')
            if len(working_string) != 2:
                continue
            try:
                for term in working_string:
                    term_val = int(term)
                    this_tot *= term_val
            except Exception as e:
                continue
            total += this_tot
    return total

# part 2
def part2(data):
    class words:
        def __init__(self):
            pass
        def add_word(self, word):
            self.word = word
            
    

        
if TestA:
    tester(part1, 'a', puzzle)
    
elif TestB:
    tester(part2, 'b', puzzle)
            
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    print(ansA)
    #puzzle.answer_A = ansA