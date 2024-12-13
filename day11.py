stones= []
import time
from collections import Counter

def blink(stones):
    new_stones = []
    for s in stones:
        str_s = str(s)
        if s == 0:
            new_stones.append(1)
        elif len(str_s) % 2 == 0:
            new_stones.append(int(str_s[0:int(len(str_s)/2)]))
            new_stones.append(int(str_s[int(len(str_s)/2):len(str_s)]))
        else:
            new_stones.append(s * 2024)
    return new_stones

def fast_mutate(state): 
    counter = Counter(state) 
    new_state = Counter(counter) 
    res = 0
    for stone, count in counter.items(): 
        if count == 0: continue 
        if stone == 0: 
            new_state[0]-=count 
            new_state[1]+=count 
        elif len(str(stone)) %2 == 0: 
            digits = str(stone) 
            ld = int(digits[:len(digits)//2]) 
            rd = int(digits[len(digits)//2:]) 
            new_state[stone]-=count 
            new_state[ld]+=count 
            new_state[rd]+=count 
        else: 
            new_state[stone*2024]+=count 
            new_state[stone]-=count 
    
    nz = [(n, v) for n, v in new_state.items() if v>0]
    res = sum([v[1] for v in nz])
    
    return new_state, res

with open("day11-data.txt") as f:

    stones = [int(i) for i in f.read().split()]

# Day 1
#print('0', len(stones), stones)
t1 =time.time()
part1 = []
original_stones = stones
for n in range (0, 25):
    stones = blink(stones)
    stones.sort()
    print(n+1, len(stones))
    if n+1 == 6:
        print(stones)

t2 =time.time()

print("Day11, part 1 = ", len(stones), " time = ", t2-t1)

stones = original_stones

# Day 2
t1 =time.time()
state = Counter(stones)
tot = 0
for n in range (0, 75):
    state, tot = fast_mutate(state)
    print(n+1, tot)

t2 =time.time()
print("Day11, part 2 = ", tot, " time = ", t2-t1)