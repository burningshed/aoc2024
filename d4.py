#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from tester import tester, Example
import numpy as np

# Each day
Day = 4
Year = 2024
ReadyA = False
ReadyB = False
TestA = True
TestB = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    data = data.lower()
    str_arr = data.splitlines()
    chr_arr = []
    for line in data.splitlines():
        chr_arr.append([c for c in line])
    str_arr_np = np.array(str_arr)
    chr_arr_np = np.array(chr_arr)
    def get_xmas(substring):
        return substring.count("xmas")
    def get_xmases(substring_arr):
        cur_tot = 0
        for line in substring_arr:
            cur_tot += get_xmas(line)
        for line in substring_arr:
            cur_tot += get_xmas(line[::-1])
        return cur_tot
    def unnumpy(numpy_arr):
        new_arr = np.array2string(numpy_arr, separator='').replace('\'','').replace('[','').replace(']','')
        print(new_arr)
        return new_arr
    total = 0
    # foreward and back
    for line in chr_arr_np:
        total += get_xmases(unnumpy(line))
    # build angle 90
    print()
    rot_arr = np.rot90(chr_arr_np)
    for line in rot_arr:
        total += get_xmases(unnumpy(line))
    # get diagonals
    print()
    def get_diag_xmas(x_arr):
        diags_d, diags_a = x_arr.shape[0], x_arr.shape[1]
        cur_tot = 0
        for ii in range(diags_d):
            cur_tot += get_xmases(unnumpy(x_arr.diagonal(ii)))
        for ii in range(diags_a-1):
            cur_tot += get_xmases(unnumpy(x_arr.diagonal(-1-ii)))
        return cur_tot
    
    total += get_diag_xmas(chr_arr_np)
    total += get_diag_xmas(np.fliplr(chr_arr_np))
    #total -= get_xmases(unnumpy(chr_arr_np.diagonal()))
    return str(total)
    
        
# part 2
def part2(data):
    pass

custom_example = [
    Example(
        """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX""", 
        '18', 
        None
        ),
    Example(
        """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
        None,
        None
        )
    ]

if TestA:
    tester(part1, 'a', puzzle, custom_example)
    
elif TestB:
    tester(part2, 'b', puzzle)
            
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    puzzle.answer_A = ansA