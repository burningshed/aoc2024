#!/usr/bin/env python3

# Imports
from aocd.models import Puzzle
from aocd.models import User
from aocd import submit
from tester import tester, Example
import math
import time

# Each day
Day = 9
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
    class Hard_Disk:
        def __init__(self, raw):
            self.stream = raw
            self.front_pointer = 0
            self.rear_pointer = len(raw) - 1
            if len(self.stream) % 2 == 0:
                self.rear_pointer - 1
            self.rear_place_in_file = 0
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.next_data = True
            self.check_sum = 0
            self.num_files = math.ceil(len(self.stream)/2)-1
            self.rear_pointer_file_num = self.num_files
            self.front_pointer_file_num = 0
            self.cur_index = 0
        def next_step(self):
            if self.front_pointer > self.rear_pointer:
                self.print_stats()
                print("New File already exhausted")
                return False
            if self.front_pointer == self.rear_pointer:
                file_size_remaining = self.rear_pointer_file_size
                for _ in range(file_size_remaining):
                    self.check_sum += self.front_pointer_file_num * self.cur_index
                    self.cur_index += 1
                return False
            if self.next_data:
                self.next_data = False
                file_size = int(self.stream[self.front_pointer])
                for _ in range(file_size):
                    self.check_sum += self.front_pointer_file_num * self.cur_index
                    self.cur_index += 1
                self.front_pointer += 1
                self.front_pointer_file_num += 1
                return True
            else:
                self.next_data = True
                empty_size = int(self.stream[self.front_pointer])
                print(empty_size)
                for _ in range(empty_size):
                    while self.rear_pointer_file_size == 0 and self.rear_pointer > self.front_pointer:
                        self.advance_rear()
                    if self.rear_pointer < self.front_pointer:
                        break
                    self.check_sum += self.cur_index * self.rear_pointer_file_num
                    self.rear_pointer_file_size -= 1
                    self.cur_index += 1
                self.front_pointer += 1
            return True
        def advance_rear(self):
            print("advancing rear!")
            self.print_stats()
            self.rear_pointer -= 2
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.rear_pointer_file_num -= 1
            self.print_stats()
        def reverse_rear(self):
            print("reversing rear")
            self.print_stats()
            self.rear_pointer += 2
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.rear_pointer_file_num += 1
            self.print_stats()
        
        def roll_back(self, roll_back_dist):
            roll_back_index = self.cur_index - 1
            for ii in range(roll_back_dist):
                self.check_sum -= (roll_back_index - ii) * self.rear_pointer_file_num
                
                

        def print_stats(self, Front=True, Rear=True):
            print("\nCurrent Stats:")
            print(f"Current Index: {self.cur_index}, Current Checksum: {self.check_sum}")
            if Front:
                print(f"Front Pointer:\nFront Pointer Location: {self.front_pointer}, File Number: {self.front_pointer_file_num}, File Size: {self.rear_pointer_file_size}")
            if Rear:
                print(f"Rear Pointer:\nRear Pointer Location: {self.rear_pointer}, File Number: {self.rear_pointer_file_num}, Remaining Size: {self.rear_pointer_file_size}")
            print()

        def print(self):
            print(self.check_sum)

                
                
    hd = Hard_Disk(data)
    while hd.next_step():
        hd.print_stats()
        pass
    hd.print()
        
    return str(hd.check_sum)
# part 2
def part2(data):
    class Hard_Disk:
        def __init__(self, raw):
            # Create hard drive object from data
            # initial attributes - front pointer at front of stream, rear pointer at back
            # holding all the file numbers not yet processed.
            self.stream = raw
            self.front_pointer = 0
            self.true_rear_pointer = len(raw) - 1
            if len(self.stream) % 2 == 0:
                self.true_rear_pointer - 1
            self.rear_pointer = self.true_rear_pointer
            self.rear_place_in_file = 0
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.next_data = True
            self.check_sum = 0
            self.num_files = math.ceil(len(self.stream)/2)-1
            self.rear_pointer_file_num = self.num_files
            self.front_pointer_file_num = 0
            self.cur_index = 0
            self.unprocessed_nums = set()
            self.unprocessed_nums.update(range(self.rear_pointer_file_num+1))
        def next_step(self):
            """One step of checksum generation. Each iteration finds the checksum for the next digit in the provided "hard drive code"
            looks at each digit in the input, alternating between representing "files" and "empty space". Different behavior for each.

            Returns:
                Status: True if not yet done generating the checksum. False if all numbers have been processed
            """
            if len(self.unprocessed_nums) == 0:
                return False
            if self.next_data:
                #print("Front Pointer at File")
                self.next_data = False
                if self.front_pointer_file_num not in self.unprocessed_nums:
                    #print("Number already processed")
                    #print(f"Incrementing Index by {self.stream[self.front_pointer]}")
                    self.cur_index += int(self.stream[self.front_pointer])
                    self.front_pointer += 1
                    self.front_pointer_file_num += 1
                    return True
                #print("Number not yet processed")
                file_size = int(self.stream[self.front_pointer])
                #print("Before File Checksum:", self.check_sum)
                for _ in range(file_size):
                    self.check_sum += self.front_pointer_file_num * self.cur_index
                    #print(f"Adding {self.front_pointer_file_num}*{self.cur_index}={self.front_pointer_file_num*(self.cur_index)}")
                    self.cur_index += 1
                #print("After File Checksum:", self.check_sum)
                self.front_pointer += 1
                self.unprocessed_nums.remove(self.front_pointer_file_num)
                self.front_pointer_file_num += 1
                return True
            else:
                #print("Empty Space")
                self.next_data = True
                empty_size = int(self.stream[self.front_pointer])
                #print("Size:", empty_size)
                empty_size_remaining = empty_size
                while empty_size_remaining != 0:
                    #print("Empty Size Remaining: ", empty_size_remaining)
                    if self.find_file(empty_size_remaining):
                        #print(f"Found file: {self.rear_pointer_file_num}")
                        empty_size_remaining = empty_size_remaining - self.rear_pointer_file_size
                        self.unprocessed_nums.remove(self.rear_pointer_file_num)
                        #print(f"Checksum before: {self.check_sum}")
                        for _ in range(self.rear_pointer_file_size):
                            self.check_sum += self.cur_index * self.rear_pointer_file_num
                            #print(f"Adding {self.rear_pointer_file_num}*{self.cur_index}={self.rear_pointer_file_num*(self.cur_index)}")
                            self.cur_index += 1
                        #print(f"Checksum after: {self.check_sum}")
                    else:
                        #print(f"Empty size remaining: {empty_size_remaining}")
                        self.cur_index += empty_size_remaining
                        break
                self.front_pointer += 1
            return True
        def advance_rear(self):
            self.rear_pointer -= 2
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.rear_pointer_file_num -= 1
        def reverse_rear(self):
            self.rear_pointer += 2
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.rear_pointer_file_num += 1
        def reset_rear_pointer(self):
            self.rear_pointer = self.true_rear_pointer
            self.rear_pointer_file_size = int(self.stream[self.rear_pointer])
            self.rear_pointer_file_num = self.num_files
            
        def find_file(self, size):
            self.reset_rear_pointer()
            for _ in range(self.num_files):
                if self.rear_pointer_file_num not in self.unprocessed_nums:
                    #print(f"File #{self.rear_pointer_file_num} already processed")
                    self.advance_rear()
                    continue
                if self.rear_pointer_file_size <= size:
                    return True
                self.advance_rear()
            return False
                    
            
        def roll_back(self, roll_back_dist):
            roll_back_index = self.cur_index - 1
            for ii in range(roll_back_dist):
                self.check_sum -= (roll_back_index - ii) * self.rear_pointer_file_num
                
                

        def print_stats(self, Front=True, Rear=True):
            print("\nCurrent Stats:")
            print(f"Current Index: {self.cur_index}, Current Checksum: {self.check_sum}, Remaining File Nums: {self.unprocessed_nums}")
            if Front:
                print(f"Front Pointer:\nFront Pointer Location: {self.front_pointer}, File Number: {self.front_pointer_file_num}")
            if Rear:
                print(f"Rear Pointer:\nRear Pointer Location: {self.rear_pointer}, File Number: {self.rear_pointer_file_num}, Remaining Size: {self.rear_pointer_file_size}")
            print()

        def print(self):
            print(self.check_sum)

                
                
    hd = Hard_Disk(data)
    while hd.next_step():
        #hd.print_stats()
        pass
    #hd.print()
        
    return str(hd.check_sum)
    pass

custom_example = [
    Example(
        """2333133121414131402""", 
        '1928', 
        '2858'
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

start = time.time()
ansB = part2(puz_data)
end = time.time()
print(end-start) 
print(ansB)