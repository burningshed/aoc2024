#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User

# Each day
Day = 1
Year = 2023
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
    sum = 0
    for line in data.splitlines():
        first = None
        for char in line:
            if char.isnumeric():
                cur = char
                if first is None:
                    first = char
        cal = first+cur
        sum += int(cal)
    return str(sum)

# part 2
def part2(data):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
    sum = 0
    for line in data.splitlines():
        first = None
        for key in numbers.keys():
            line = line.replace(key, key+str(numbers[key])+key)
        for char in line:
            if char.isnumeric():
                cur = char
                if first is None:
                    first = char
        cal = first+cur
        sum += int(cal)
    return str(sum)


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
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    puzzle.answer_A = ansA