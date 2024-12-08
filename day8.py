from itertools import combinations
import math

def print_map(m):
    print()
    for line in m:
        print(line)

def check_pair(a, b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    
    # start at point a and map out the line through point b in both directions, each until we leave the grid
    posy = a[0]
    posx = a[1]
    count = 0
    while posy >= 0 and posy < len(map) and posx >= 0 and posx < len(map[1]):
        d1 = math.sqrt((a[0]-posy) * (a[0]-posy) + (a[1]-posx) * (a[1]-posx))
        d2 = math.sqrt((b[0]-posy) * (b[0]-posy) + (b[1]-posx) * (b[1]-posx))
        if d1 == 2 * d2 or d2 == 2 * d1:
                if (posy, posx) not in antinodes:
                     antinodes.append((posy, posx))
                     count+=1
        posy += dy
        posx += dx

    posy = a[0]
    posx = a[1]
    while posy >= 0 and posy < len(map) and posx >= 0 and posx < len(map[1]):
        d1 = math.sqrt((a[0]-posy) * (a[0]-posy) + (a[1]-posx) * (a[1]-posx))
        d2 = math.sqrt((b[0]-posy) * (b[0]-posy) + (b[1]-posx) * (b[1]-posx))
        if d1 == 2 * d2 or d2 == 2 * d1:
                if (posy, posx) not in antinodes:
                     antinodes.append((posy, posx))
                     count+=1
        posy -= dy
        posx -= dx
    
    return count

def check_pair_pt2(a, b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    
    # start at point a and map out the line through point b in both directions, each until we leave the grid
    posy = a[0]
    posx = a[1]
    while posy >= 0 and posy < len(map) and posx >= 0 and posx < len(map[1]):
        if (posy, posx) not in antinodes:
            antinodes.append((posy, posx))
        posy += dy
        posx += dx

    posy = a[0]
    posx = a[1]
    while posy >= 0 and posy < len(map) and posx >= 0 and posx < len(map[1]):
        if (posy, posx) not in antinodes:
            antinodes.append((posy, posx))
        posy -= dy
        posx -= dx
    
    return


map = []
antenna_dict = {}
with open("day8-data.txt") as f:

    # Read the file and initialise the start pos
    i = 0
    for line in f.readlines():
        map.append(line.strip('\n'))
        j = 0
        for j in range(0,len(line)):
            if line[j].isalnum():
                if line[j] in antenna_dict:
                    antenna_dict[line[j]].append((i, j))
                else:
                    antenna_dict[line[j]] = [(i,j)]
            j+=1
        i+=1

# Part 1
antinodes = []
for a in antenna_dict:
    pairs = combinations(antenna_dict[a], 2)
    for p in pairs:
        check_pair(p[0], p[1])

print("Day8, part1 = ", len(antinodes))

# Part 2
antinodes = []
for a in antenna_dict:
    pairs = combinations(antenna_dict[a], 2)
    for p in pairs:
        check_pair_pt2(p[0], p[1])

print("Day8, part2 = ", len(antinodes))