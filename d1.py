#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User

# Each day
Day = 1
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
    listA = []
    listB = []
    for line in data.splitlines():
        terms = line.split()
        listA.append(int(terms[0]))
        listB.append(int(terms[1])) 
    listA.sort()
    listB.sort()
    num = 0
    sum = 0
    for term in listA:
        sum += abs(term - listB[num])
        num += 1
    return str(sum)
# part 2
def part2(data):
    listA = []
    listB = dict()
    
    for line in data.splitlines():
        terms = line.split()
        listA.append(int(terms[0]))
        try:
            listB[int(terms[1])] += 1
        except:
            listB[int(terms[1])] = 1
    tot = 0
    for term in listA:
        try:
            tot += listB[term] * term
        except:
            continue
    return str(tot)

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
        try:
            ans = part2(e_data)
        except Exception as e:
            print(e)
            working = False
        if ans != '31':
            working = False
            print("Incorrect Output")
            print(f"Expected: {31}\nActual: {ans}")
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