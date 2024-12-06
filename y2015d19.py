#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example

# Each day
Day = 19
Year = 2015
ReadyA = False
ReadyB = False
TestA = False
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
    rules_str, starter = data.split("\n\n")
    rules = dict()
    for rule_str in rules_str.splitlines():
        origin, dest = rule_str.split(" => ")
        rules[origin] = rules.get(origin, []) + [dest]

    def scanner(mol_str, target):
        new_mols = []
        loc = mol_str.find(target)
        length = len(target)
        while loc != -1:
            for replacement in rules[target]:
                new_mol = mol_str[:loc] + mol_str[loc:].replace(target, replacement, 1)
                new_mols = new_mols + [new_mol]
            loc = mol_str.find(target, loc+length)
        return new_mols
                
            
    poss_targets = set()
    for key in rules:
        new_mols = scanner(starter, key)
        poss_targets.update(new_mols)
    count = len(poss_targets)
    return str(count) 
# part 2
def part2(data):
    rules_str, starter = data.split("\n\n")
    final_target = 'e'
    rules = dict()
    for rule_str in rules_str.splitlines():
        dest, origin = rule_str.split(" => ")
        rules[origin] = rules.get(origin, []) + [dest]

    def scanner(mol_str, target):
        new_mols = []
        loc = mol_str.find(target)
        length = len(target)
        while loc != -1:
            for replacement in rules[target]:
                new_mol = mol_str[:loc] + mol_str[loc:].replace(target, replacement, 1)
                new_mols = new_mols + [new_mol]
            loc = mol_str.find(target, loc+length)
        return new_mols
                
            
    def update(start_mol):
        poss_targets = set()
        for key in rules:
            new_mols = scanner(start_mol, key)
            poss_targets.update(new_mols)
        return poss_targets
    def step(begin_set):
        new_targets = set()
        for mol in begin_set:
            new_targets.update(update(mol))
        return new_targets
        
    steps = 1
    mols = step(set([starter]))
    Done = False
    while not Done:
        mols = step(mols)
        steps += 1
        Done = final_target in mols
        if steps > 7:
            Done = True
            
    print(mols)
    return str(steps)
    
        
    

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
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    submit(ansA, part='a', year=2015, day=19, session=token)