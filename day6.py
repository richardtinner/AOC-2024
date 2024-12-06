import copy
import time

def print_map(m):
    print()
    for line in m:
        print(line)

def update_map(row, col, symbol):
    map[row] = map[row][0:col] + symbol + map[row][col+1:len(map[row])]

def get_move(row, col):
    dir = map[row][col]
    move = (0, 0, dir)
    if dir == '^':
        if row != 0:
            if map[row-1][col] != '#':
                move = (-1, 0, '^')
                update_map(row-1, col, '^')
                update_map(row, col, 'X')
            else:
                move = (0, 0, '>')
                update_map(row, col, '>')
        else:
            update_map(row, col, 'X')
            move = (-1, 0, '^')
        
    elif dir == 'v':
        if row != len(map) - 1:
            if map[row+1][col] != '#':
                move = (1, 0, 'v')
                update_map(row+1, col, 'v')
                update_map(row, col, 'X')
            else:
                move = (0, 0, '<')
                update_map(row, col, '<')
        else:
            update_map(row, col, 'X')
            move = (1, 0, 'v')

    elif dir == '>':
        if col != len(map[0]) - 1:
            if map[row][col+1] != '#':
                move = (0, 1, '>')
                update_map(row, col+1, '>')
                update_map(row, col, 'X')
            else:
                move = (0, 0, 'v')
                update_map(row, col, 'v')
        else:
            update_map(row, col, 'X')
            move = (0, 1, '>')
                
    elif dir == '<':
        if col != 0:
            if map[row][col-1] != '#':
                move = (0, -1, '<')
                update_map(row, col-1, '<')
                update_map(row, col, 'X')
            else:
                move = (0, 0, '^')
                update_map(row, col, '^')
        else:
            update_map(row, col, 'X')
            move = (0, -1, '<')
                
    return move
    

start_time =time.time()
map = []
start_row = start_col = 0
with open("day6-data.txt") as f:

    # Read the file and initialise the start pos
    i = 0
    for line in f.readlines():
        map.append(line.strip('\n'))
        if line.find('>') != -1:
            start_col = line.find('>')
            start_row = i
        elif line.find('<') != -1:
            start_col = line.find('<')
            start_row = i
        elif line.find('^') != -1:
            start_col = line.find('^')
            start_row = i
        elif line.find('v') != -1:
            start_col = line.find('v')
            start_row = i
        i += 1

original_map = copy.deepcopy(map)
row = start_row
col = start_col

# Day 1
while row > -1 and row < len(map) and col > -1 and col < len(map[0]):

    move = get_move(row, col)
    row += move[0]
    col += move[1]

sum = 0 
for row in map:
    sum += row.count('X')

part1_time = time.time()
print("Day 6, part 1 = ", sum, "time = ", part1_time - start_time)

# Day 2
# Iterate over grid placing an obstacle at every square and seeing if as loop is created
part1_map = copy.deepcopy(map)
sum = 0
for i in range(0, len(part1_map)):
    for j in range(0, len(part1_map[0])):
        if part1_map[i][j] == 'X' and not (i == start_row and j == start_col):
            map = copy.deepcopy(original_map)
            path = {}
            map[i] = map[i][0:j] + '#' + map[i][j+1:len(map[i])]
            row = start_row
            col = start_col
            loop = False
            while row > -1 and row < len(map) and col > -1 and col < len(map[0]) and not loop:
                move = get_move(row, col)
                row += move[0]
                col += move[1]

                # need to check if we are in a loop
                if (row, col) in path:
                    if move[2] in path[(row, col)]:
                        loop = True
                    else:
                        path[(row, col)].append(move[2])
                else:
                    path[(row, col)] = [move[2]]
            
            if loop:
                sum += 1

part2_time = time.time()
print("Day 6, part 2 = ", sum, "time = ", part2_time - part1_time)


                




