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
TestA = False
TestB = True

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
        cur_tot += get_xmas(substring_arr)
        cur_tot += get_xmas(substring_arr[::-1])
        return cur_tot
    def unnumpy(numpy_arr):
        new_arr = np.array2string(numpy_arr, separator='').replace('\'','').replace('[','').replace(']','').replace('\n','').replace(" ","")
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
    print()
    total += get_diag_xmas(np.fliplr(chr_arr_np))
    #total -= get_xmases(unnumpy(chr_arr_np.diagonal()))
    return str(total)
    
        
# part 2
def part2(data):
    data = data.lower()
    str_arr = data.splitlines()
    chr_arr = []
    for line in data.splitlines():
        chr_arr.append([c for c in line])
    str_arr_np = np.array(str_arr)
    chr_arr_np = np.array(chr_arr)
    def unnumpy(numpy_arr):
        new_arr = np.array2string(numpy_arr, separator='').replace('\'','').replace('[','').replace(']','').replace('\n','').replace(" ","")
        print(new_arr)
        return new_arr
    def check_corner(arr, index, cor):
        print(index, cor)
        cur_index = index + cor
        print(index, cor, cur_index)
        opp_index = index + np.array(cor) * -1
        print(opp_index, index, cor, cur_index)
        if arr[cur_index[0],cur_index[1]] == 'm' and arr[opp_index[0], opp_index[1]] == 's':
            return True
        if arr[cur_index[0],cur_index[1]] == 's' and arr[opp_index[0], opp_index[1]] == 'm':
            return True
        return False
    def check_corners(arr, index):
        main_corners = [(-1,-1), (-1,1)]
        for corner in main_corners:
            if check_corner(arr, index, corner):
                continue
            else:
                return False
        return True
                
                
        print(arr[index[0], index[1]])
    total = 0
    
    print(chr_arr_np)
    active_chr_arr_np = chr_arr_np[1:-1,1:-1]
    print(active_chr_arr_np)
    a_list = np.argwhere(active_chr_arr_np=='a')+1
    for element in a_list:
        if check_corners(chr_arr_np, element):
            total += 1
    print()
    return str(total)
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
        '9'
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
        '18',
        '9'
        ),
    Example(
    """MXMAS
xMMMM
MmAMX
AsAmx
sXXsX""",
    '4',
    None
    )
    ]

if TestA:
    tester(part1, 'a', puzzle, custom_example)
    
elif TestB:
    tester(part2, 'b', puzzle, custom_example)
            
print(part2(puz_data))
            
            
# solution and submit
if ReadyB:
    ansB = part2(puz_data)
    puzzle.answer_B = ansB 
    
elif ReadyA:
    ansA = part1(puz_data)
    puzzle.answer_A = ansA