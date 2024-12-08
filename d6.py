#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import time

# Each day
Day = 6
Year = 2024
ReadyA = False
ReadyB = False
TestA = False
TestA_custom = False
TestB = False
TestB_custom = False

# get puzzle 
token = open("./.config/aocd/token", 'r').read()
user = User(token)
puzzle = Puzzle(Year, Day, user)
puz_data = puzzle.input_data

# Part 1
def part1(data):
    class coord:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.tup = (x,y)
            
        def __eq__(self, other):
            if isinstance(other, coord):
                if self.x == other.x and self.y == other.y:
                    return True
                return False
            else:
                print(f"warning! comparing coord to non-coord \nNon-coord is of type {other}")
                return False
        
        def __hash__(self) -> int:
            return hash(self.tup)
        
        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return coord(x,y)
                        
        def __str__(self) -> str:
            return f"{self.x, self.y}"
        def __repr__(self) -> str:
            return self.__str__()
        
        def __gt__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x > other.x and self.y > other.y:
                return True
            return False
            
        def __ge__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x > other.x or self.y > other.y:
                return True
            return False
        def __lt__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x < other.x and self.y < other.y:
                return True
            return False
            
        def __le__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x < other.x or self.y < other.y:
                return True
            return False
                        
    visited = set()
    guard_syms= "^><vV"
    obs_sym = "#"
    dir_dict = {
        '^': coord(0,-1), 
        '>': coord(1,0),
        'v': coord(0,1),
        'V': coord(0,1),
        '<': coord(-1,0)
        }
    rot_dict = {
        '^': ">", 
        '>': "V",
        'v': "<",
        'V': "<",
        '<': "^"
        }
    guard_loc = None
    obs_locs = set()
    yy = 0
    for line in data.splitlines():
        xx = 0
        for symbol in line:
            if symbol in guard_syms:
                guard_loc = coord(xx, yy)
                guard_dir = symbol
            elif symbol == obs_sym:
                obs_locs.add(coord(xx, yy))
            xx += 1
        yy += 1
    bounds = [coord(xx-1, yy-1), coord(0,0)]
    

    def step(cur_loc, cur_dir):
        next_step = cur_loc + dir_dict[cur_dir]
        moved = 0
        if next_step in obs_locs:
            print(f"obsticle detected! turning! {cur_dir} to {rot_dict[cur_dir]}")
            cur_dir = rot_dict[cur_dir]
        else:
            cur_loc = next_step
            moved += 1
        return cur_loc, cur_dir, moved
    steps = 0
    oob = False
    while not oob:
        visited.add(guard_loc)
        guard_loc, guard_dir, moved = step(guard_loc, guard_dir)
        steps += moved
        if guard_loc >= bounds[0] or guard_loc <= bounds[1]:
            print("oob")
            oob = True
        
    return str(len(visited))
                
            
# part 2
def part2(data):
    class coord:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.tup = (x,y)
            
        def __eq__(self, other):
            if isinstance(other, coord):
                if self.x == other.x and self.y == other.y:
                    return True
                return False
            if other == None:
                return False
            else:
                print(f"warning! comparing coord to non-coord \nNon-coord is of type {other}")
                return False
        
        def __hash__(self) -> int:
            return hash(self.tup)
        
        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return coord(x,y)
                        
        def __str__(self) -> str:
            return f"{self.x, self.y}"
        def __repr__(self) -> str:
            return self.__str__()
        
        def __gt__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x > other.x and self.y > other.y:
                return True
            return False
            
        def __ge__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x > other.x or self.y > other.y:
                return True
            return False
        def __lt__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x < other.x and self.y < other.y:
                return True
            return False
            
        def __le__(self, other):
            if not isinstance(other, coord):
                raise Exception
            if self.x < other.x or self.y < other.y:
                return True
            return False
                        
    guard_syms= "^><vV"
    obs_sym = "#"
    dir_dict = {
        '^': coord(0,-1), 
        '>': coord(1,0),
        'v': coord(0,1),
        'V': coord(0,1),
        '<': coord(-1,0)
        }
    rot_dict = {
        '^': ">", 
        '>': "V",
        'v': "<",
        'V': "<",
        '<': "^"
        }
    
    visited = set()
    guard_loc = None
    obs_locs = set()
    
    yy = 0
    for line in data.splitlines():
        xx = 0
        for symbol in line:
            if symbol in guard_syms:
                guard_loc = coord(xx, yy)
                guard_dir = symbol
            elif symbol == obs_sym:
                obs_locs.add(coord(xx, yy))
            xx += 1
        yy += 1
    bounds = [coord(xx-1, yy-1), coord(0,0)]
    

    def step(cur_loc, cur_dir, extra_obs = None):
        next_step = cur_loc + dir_dict[cur_dir]
        moved = 0
        if next_step in obs_locs or next_step == extra_obs:
            cur_dir = rot_dict[cur_dir]
        else:
            cur_loc = next_step
        return cur_loc, cur_dir
    def first_run(start_loc, start_dir):
        visited = set()
        guard_loc = start_loc
        guard_dir = start_dir
        oob = False
        while not oob:
            visited.add(guard_loc)
            guard_loc, guard_dir = step(guard_loc, guard_dir)
            if guard_loc >= bounds[0] or guard_loc <= bounds[1]:
                oob = True
        return visited
    visited = first_run(guard_loc, guard_dir)
    class loop_checker:
        def __init__(self):
            self.pot_loops = set()
            pass
        def check(self, loc, dir):
            loop = (loc, dir)
            if loop in self.pot_loops:
                return True
            else:
                self.pot_loops.add(loop)
    def future_run(start_loc, start_dir, new_obs):
        guard_loc = start_loc
        guard_dir = start_dir
        oob = False
        lc = loop_checker()
        while not oob:
            if lc.check(guard_loc, guard_dir):
                return True
            guard_loc, guard_dir = step(guard_loc, guard_dir, new_obs)
            if guard_loc >= bounds[0] or guard_loc <= bounds[1]:
                oob = True
        return False
            
    count = 0
    for loc in visited:
        if loc == guard_loc:
            continue
        if future_run(guard_loc, guard_dir, loc):
            count += 1

    
     
    return str(count)

custom_example = [
    Example(
        """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""", 
        'answer_a', 
        '6'
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

    
ansA = part1(puz_data)
print(ansA)
start = time.time()
ansB = part2(puz_data)
end = time.time()
print(end - start)