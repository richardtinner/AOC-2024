def print_map(m):
    for row in m:
        for v in row:
            print(v, end='')
        print()
    return

def get_valid_moves(map, pos):
    vm = []
    current = map[pos[0]][pos[1]]
    if pos[0] > 0 and map[pos[0]-1][pos[1]] == current+1:
        vm.append((pos[0]-1, pos[1]))
    if pos[0] < len(map)-1 and map[pos[0]+1][pos[1]] == current+1:
        vm.append((pos[0]+1, pos[1]))
    if pos[1] > 0 and map[pos[0]][pos[1]-1] == current+1:
        vm.append((pos[0], pos[1]-1))
    if pos[1] < len(map[0])-1 and map[pos[0]][pos[1]+1] == current+1:
        vm.append((pos[0], pos[1]+1))
    return vm

map = []
trailheads = []
with open("day10-data.txt") as f:

    # Read the file, initialise the map and find the trailheads
    row = 0
    for line in f.readlines():
        res = [int(i) for i in line.strip('\n')]
        map.append(res)
        while(line.find('0')!=-1): 
            trailheads.append((row, line.find('0')))
            line = line.replace('0', '*', 1)
        row += 1


# Part 1
total = 0
for th in trailheads:
    moves  = []
    visited = []
    score = 0
    moves.extend(get_valid_moves(map, th))
    while len(moves) > 0:
        new_pos = moves.pop()
        if new_pos not in visited:
            if map[new_pos[0]][new_pos[1]] == 9:
                score += 1
            else:
                moves.extend(get_valid_moves(map, new_pos))
        visited.append(new_pos)
    
    total += score

print("Day 10, part 1 score = ", total)

# Part 2
total = 0
for th in trailheads:
    moves  = []
    visited = []
    score = 0
    moves.extend(get_valid_moves(map, th))
    while len(moves) > 0:
        new_pos = moves.pop()
        if map[new_pos[0]][new_pos[1]] == 9:
            score += 1
        else:
            moves.extend(get_valid_moves(map, new_pos))
        visited.append(new_pos)

    total += score

print("Day 10, part 2 score = ", total)

