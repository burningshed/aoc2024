#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from tester import tester, Example

# Each day
Day = 5
Year = 2024
ReadyA = False
ReadyB = False
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
    rules, updates = data.split("\n\n")
    key_before_val = dict()
    key_after_val = dict()
    def rule_check(update, rule_dict):
        for ii in range(len(update)):
            if update[ii] not in key_after_val:
                continue
            ban_list = key_after_val[update[ii]]
            for page in update[ii:]:
                if page in ban_list:
                    return False
        return True
        
    for rule in rules.splitlines():
        first, second = rule.split("|")
        key_before_val[first] = key_before_val.get(first, []) + [second]
        key_after_val[second] = key_after_val.get(second, []) + [first]
    total = 0
    for line in updates.splitlines():
        update = line.split(",")
        if rule_check(update, key_after_val):
            total += int(update[len(update) // 2])
    
    return str(total)
        
        
# part 2
def part2(data):
    rules, updates = data.split("\n\n")
    key_before_val = dict()
    key_after_val = dict()
    def rule_check(update, rule_dict):
        for ii in range(len(update)):
            if update[ii] not in key_after_val:
                continue
            ban_list = key_after_val[update[ii]]
            for page in update[ii:]:
                if page in ban_list:
                    return False
        return True
    
    def rule_fix(update):
        changed = False
        for ii in range(len(update)):
            if update[ii] not in key_after_val:
                continue
            new_update = update[:ii]
            print(new_update)
            new_update_end = []
            # ban_list - all the pages that should come before key
            ban_list = key_after_val[update[ii]]
            for page in update[ii:]:
                if page in ban_list:
                    new_update.append(page)
                    print(new_update)
                    changed = True
                else:
                    new_update_end.append(page)
            if changed:
                update = new_update.copy() + new_update_end.copy()
                return changed, update
        return changed, update
        
    for rule in rules.splitlines():
        first, second = rule.split("|")
        key_before_val[first] = key_before_val.get(first, []) + [second]
        key_after_val[second] = key_after_val.get(second, []) + [first]
    total = 0
    for line in updates.splitlines():
        update = line.split(",")
        if not rule_check(update, key_after_val):
            any_changes, update = rule_fix(update)
            while any_changes:
                any_changes, update = rule_fix(update)
            print(update)
            total += int(update[len(update) // 2])
    
    return str(total)

custom_example = [
    Example(
        """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""", 
        None, 
        '123'
        )
    ]

if TestA:
    tester(part1, 'a', puzzle)

if TestA_custom:
    tester(part1, 'a', puzzle, custom_example)
    
if TestB:
    tester(part2, 'b', puzzle)
    
if TestB_custom:
    tester(part2, 'b', puzzle, custom_example, debug_mode=False)        
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    puzzle.answer_A = ansA