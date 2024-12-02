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

## Part A
if TestA:
    print("Testing Part A")
    num = 1
    for example in puzzle.examples:
        print(f"~~~~~~~~~ Example {num} ~~~~~~~~~~")
        e_data = example.input_data
        if example.answer_a == None:
            print("Example has no part A\n")
            num += 1
            continue
        try:
            ans = part1(e_data)
        except Exception as e:
            print(e)
            working = False
        if ans != example.answer_a:
            working = False
            print("Incorrect Output")
            print(f"Expected: {example.answer_a}\nActual: {ans}")
        else:
            print(f"Example {num} Passed")
        num += 1
        print("")

    if working:
        ansA = part1(puz_data)
        print(f"Part A Answer: {ansA}")

## Part B
if TestB:
    print("Testing Part B")
    num = 1
    for example in puzzle.examples:
        print(f"~~~~~~~~~ Example {num} ~~~~~~~~~~")
        e_data = example.input_data
        if example.answer_b == None:
            num += 1
            print("Example has no part B\n")
            continue
        try:
            ans = part2(e_data)
        except Exception as e:
            print(e)
            working = False
        if ans != example.answer_b:
            working = False
            print("Incorrect Output")
            print(f"Expected: {example.answer_b}\nActual: {ans}")
        else:
            print(f"Example {num} Passed")
        num += 1
        print("")

    if working:
        ansB = part2(puz_data)
        print(f"Part B Answer: {ansB}")
        
        
def tester(solver, part, puz):
    print(f"Testing part {part}")
    working = True
    
    # Define Example Data Location from Puzzle
    def get_answer(cur_example, cur_part):
        if cur_part == 'a':
            return cur_example.answer_a
        elif cur_part == 'b':
            return cur_example.answer_b
            
    # Run through each example
    num = 1
    for example in puz.examples:
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
            working = False
            print("Error!")
            print(e)
            num += 1
            continue
        if ans != e_answer:
            working = False
            print("Incorrect Output!")
            print(f"Expected: {e_answer}\n\n Solver Output: {ans}\n")
        else:
            print("Example Passed!")
        num += 1
        print("")
        
    if working:
        print("Running Real Input")
        try:
            ans = solver(puz.input_data)
            print(ans)
            return True
        except Exception as e:
            print("Error!")
            print(e)
    return False
            
        
            
            
            
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    puzzle.answer_A = ansA