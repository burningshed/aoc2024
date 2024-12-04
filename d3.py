#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from tester import tester, Example
import re

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
    class Comp:
        def __init__(self):
            self.on = True
            self.total = 0

        def do(self):
            self.on = True

        def dont(self):
            self.on = False
        
        def mul(self, a, b):
            if self.on:
                self.total += a * b
                
        
    class Word:
        def __init__(self, re_string, label, func):
            self.re_string = re_string
            self.label = label
            self.func = func
    class Words:
        def __init__(self):
            self.word_list = dict()
            pass
        def add_word(self, word):
            self.word_list[word.label] = word
            
        def get_words_re(self):
            return r"|".join(self.word_list[x].re_string for x in self.word_list)

    def scanner(data_string, words):
        word_search_re = re.compile(words.get_words_re()) 
        results = word_search_re.finditer(data_string)
        for result in results:
            if result.group("mul"):
                words.word_list["mul"].func(int(result.group("arg1")),int(result.group("arg2")))
            elif result.group("dont"):
                words.word_list["dont"].func()
            elif result.group("do"):
                words.word_list["do"].func()
            
    mul_re = r"(?P<mul>mul\((?P<arg1>\d+),(?P<arg2>\d+)\))"
    dont_re = r"(?P<dont>don't\(\))"
    do_re = r"(?P<do>do\(\))"
    words = Words()
    comp = Comp()
    words.add_word(Word(mul_re, "mul", comp.mul))
    words.add_word(Word(dont_re, "dont", comp.dont))
    words.add_word(Word(do_re, "do", comp.do))

    scanner(data, words)
    return str(comp.total)
        
            
re_Example = [Example("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", '161', None), 
              Example("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", '161', '48')]

        
if TestA:
    tester(part1, 'a', puzzle)
    
elif TestB:
    tester(part2, 'b', puzzle, re_Example)
            
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    print(ansA)
    #puzzle.answer_A = ansA