#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User

# Each day
Day = None
Year = None
ReadyA = False
ReadyB = False
TestA = False
TestB = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    pass
# part 2
def part2(data):
    pass

# testing
working = True
        
        
class Example:
    def __init__(self, input_data, answer_a, answer_b):
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.input_data = input_data

def tester(solver, part, puz, custom_examples=None, debug_mode=False):
    print(f"Testing part {part}")
    
    if custom_examples == None:
        examples = puz.examples
    else:
        examples = custom_examples
    # Define Example Data Location from Puzzle
    def get_answer(cur_example, cur_part):
        if cur_part == 'a':
            return cur_example.answer_a
        if cur_part == 'b':
            return cur_example.answer_b
            
    # Run through each example
    num = 1
    for example in examples:
        print(f"~~~~~~ Example {num} ~~~~~~~\n")
        print(example)
        print("")
        e_data = example.input_data
        e_answer = get_answer(example, part)
        if e_answer == None:
            num += 1
            print(f"Example has no answer for part {part}")
            continue
        try:
            ans = solver(e_data)
        except Exception as e:
            # Turn on debug mode if exception thrown
            debug_mode = True
            print("Error!")
            print(e)
            num += 1
            continue
        if ans != e_answer:
            # Turn on debug mode if output doesn't match
            debug_mode = True
            print("Incorrect Output!")
            print(f"Expected: {e_answer}\n\n Solver Output: {ans}\n")
        else:
            print("Example Passed!")
        num += 1
        print("")
        
    # run code on real input if debug mode not set
    if not debug_mode:
        print("Running Real Input")
        try:
            ans = solver(puz.input_data)
            print(ans)
            return True
        except Exception as e:
            print("Error!")
            print(e)
    return False
            
        
            
            
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
    puzzle.answer_A = ansA