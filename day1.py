#!/usr/bin/env python3
from aocd.models import Puzzle
from aocd.models import User

token = open("./.config/aocd/token", 'r').read()
user = User(token)

puzzle = Puzzle(2023, 1, user)

print(puzzle.examples)
data = puzzle.input_data
# Part 1
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


# part 2
testdata = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
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

print(sum)