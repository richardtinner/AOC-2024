stones= []
import copy

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

def list_part2stones(cs, os):
    s = os
    for key, count in cs.items():
        if count > 0:
            for i in range(0, count):
                s.append(key)
    return s

with open("day11-data.txt") as f:

    stones = [int(i) for i in f.read().split()]

# Day 1
#print('0', len(stones), stones)
part1 = []
original_stones = copy.deepcopy(stones)
for n in range (0, 25):
    stones = blink(stones)
    stones.sort()
    print(n+1, len(stones))
    if n+1 == 6:
        print(stones)

print("Day11, part 1 = ", len(stones))

stones = copy.deepcopy(original_stones)

# Day 2
precalc_stones = {}
core_stones = {}
other_stones = []
for i in range(0, 1000000):
    precalc_stones[i] = blink([i])
    core_stones[i] = 0
for i in range(2024, 2024*10, 2024):
    precalc_stones[i] = blink([i])
    core_stones[i] = 0

empty_core_stones = copy.deepcopy(core_stones)
for s in stones:
    if s in core_stones:
        core_stones[s] += 1
    else:
        other_stones.append(s)


for n in range (0, 75):
    # first process core stones
    #if n+1 == 6:
    #    print("x")
    new_core_stones = copy.deepcopy(empty_core_stones)
    new_other_stones = []
    for key, count in core_stones.items():
        #if key == 10120:
        #    print("y")
        if count > 0:
            for s in precalc_stones[key]:
                if s in new_core_stones:
                    new_core_stones[s] += count
                else:
                    for i in range(0, count):
                        new_other_stones.append(s)


        
    # then process other stones
    other_stones = blink(other_stones)
    for s in other_stones:
        if s in new_core_stones:
            new_core_stones[s] += 1
        else:
            new_other_stones.append(s)
    
    core_stones = copy.deepcopy(new_core_stones)
    other_stones = copy.deepcopy(new_other_stones)
    cs = copy.deepcopy(new_core_stones)
    os = copy.deepcopy(new_other_stones)

    s = list_part2stones(cs, os)
    s.sort()
    print(n+1, len(s))
    #if n+1 == 6:
    #    print(s)



part2_len = len(other_stones)
for key, count in core_stones.items():
    if count > 0:
        part2_len += count

print("Day11, part 2 = ", part2_len)