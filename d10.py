#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import numpy as np
from AoCHelpers import coord

# Each day
Day = 10
Year = 2024
ReadyA = False
ReadyB = True
TestA = False
TestA_custom = True
TestB = False
TestB_custom = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    #data = data.replace('.','-2')
    directions = np.array([(0,1),(0,-1),(-1,0),(1,0)])
    data = np.array([[int(x) for x in y] for y in data.splitlines()])
    print(data)
    hilltops = np.argwhere(data==9)
    print(data.shape)
    print(hilltops)
    

    def find_trail(trail_map, sp, slope=-1, goal=0):
        # check if done
        if trail_map[sp[0],sp[1]] == goal:
            goal_loc = set()
            goal_loc.add(coord(int(sp[0]),int(sp[1])))
            return 1, goal_loc
        poss_next = sp + directions
        # check map boundries
        x_valid = np.logical_and(poss_next[:,0] >= 0, poss_next[:,0] < trail_map.shape[0])
        y_valid = np.logical_and(poss_next[:,1] >= 0, poss_next[:,1] < trail_map.shape[1])
        valid = np.logical_and(x_valid, y_valid)
        poss_next = poss_next[valid]
        # check slope
        cur_height = trail_map[sp[0],sp[1]]
        target_height = cur_height + slope
        valid_heights = trail_map[poss_next[:,0],poss_next[:,1]] == target_height
        poss_next = poss_next[valid_heights]
        # check if nowhere else to go
        if len(poss_next) == 0:
            return 0, set()
        paths_found = 0
        goal_locations = set()
        for spot in poss_next:
            new_paths, new_goal_locations = find_trail(trail_map, spot, slope, goal)
            paths_found += new_paths
            goal_locations.update(new_goal_locations)
        return paths_found, goal_locations

    paths = 0
    u_paths = 0
    for hilltop in hilltops:
        new_paths, gl = find_trail(data, hilltop)
        paths += new_paths
        u_paths += len(gl)
    trailheads = np.argwhere(data==0)
    print(paths)
    print(u_paths)
    
    paths = 0
    u_paths = 0
    for trailhead in trailheads:
        new_paths, gl = find_trail(data, trailhead, slope=1, goal=9)
        paths += new_paths
        u_paths += len(gl)
    print(paths, u_paths)
    return str(u_paths)
    pass
# part 2
def part2(data):
    #data = data.replace('.','-2')
    directions = np.array([(0,1),(0,-1),(-1,0),(1,0)])
    data = np.array([[int(x) for x in y] for y in data.splitlines()])
    print(data)
    hilltops = np.argwhere(data==9)
    print(data.shape)
    print(hilltops)
    

    def find_trail(trail_map, sp, slope=-1, goal=0):
        # check if done
        if trail_map[sp[0],sp[1]] == goal:
            goal_loc = set()
            goal_loc.add(coord(int(sp[0]),int(sp[1])))
            return 1, goal_loc
        poss_next = sp + directions
        # check map boundries
        x_valid = np.logical_and(poss_next[:,0] >= 0, poss_next[:,0] < trail_map.shape[0])
        y_valid = np.logical_and(poss_next[:,1] >= 0, poss_next[:,1] < trail_map.shape[1])
        valid = np.logical_and(x_valid, y_valid)
        poss_next = poss_next[valid]
        # check slope
        cur_height = trail_map[sp[0],sp[1]]
        target_height = cur_height + slope
        valid_heights = trail_map[poss_next[:,0],poss_next[:,1]] == target_height
        poss_next = poss_next[valid_heights]
        # check if nowhere else to go
        if len(poss_next) == 0:
            return 0, set()
        paths_found = 0
        goal_locations = set()
        for spot in poss_next:
            new_paths, new_goal_locations = find_trail(trail_map, spot, slope, goal)
            paths_found += new_paths
            goal_locations.update(new_goal_locations)
        return paths_found, goal_locations

    paths = 0
    u_paths = 0
    for hilltop in hilltops:
        new_paths, gl = find_trail(data, hilltop)
        paths += new_paths
        u_paths += len(gl)
    trailheads = np.argwhere(data==0)
    print(paths)
    print(u_paths)
    
    paths = 0
    u_paths = 0
    for trailhead in trailheads:
        new_paths, gl = find_trail(data, trailhead, slope=1, goal=9)
        paths += new_paths
        u_paths += len(gl)
    print(paths, u_paths)
    return str(paths)
    pass
    pass

custom_example = [
    Example(
        """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9""", 
        '2', 
        None
        ),
    Example(
        """..90..9
...1.98
...2..7
6543456
765.987
876....
987....""", 
        '4', 
        None
        ),
    Example(
        """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01""", 
        '3', 
        None
        ),
    Example(
        """890101237
781218747
874309657
965498747
456789037
320190127
013298017
104567329""", 
        '36', 
        None
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
    submit(ansB, part='b', day=Day, year=Year, session=token)
elif ReadyA:
    ansA = part1(puz_data)
    submit(ansA, part='a', day=Day, year=Year, session=token)