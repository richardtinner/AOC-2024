def print_map(m):
    print()
    for line in m:
        print(line)

def update_map(row, col, symbol):
    map[row] = map[row][0:col] + symbol + map[row][col+1:len(map[row])]

def get_move(row, col):
    move = (0, 0)
    dir = map[row][col]
    if dir == '^':
        if row != 0:
            if map[row-1][col] != '#':
                move = (-1, 0)
                update_map(row-1, col, '^')
                update_map(row, col, 'X')
            else:
                update_map(row, col, '>')
        else:
            update_map(row, col, 'X')
            move = (-1, 0)
        
    elif dir == 'v':
        if row != len(map) - 1:
            if map[row+1][col] != '#':
                move = (1, 0)
                update_map(row+1, col, 'v')
                update_map(row, col, 'X')
            else:
                update_map(row, col, '<')
        else:
            update_map(row, col, 'X')
            move = (1, 0)

    elif dir == '>':
        if col != len(map[0]) - 1:
            if map[row][col+1] != '#':
                move = (0, 1)
                update_map(row, col+1, '>')
                update_map(row, col, 'X')
            else:
                update_map(row, col, 'v')
        else:
            update_map(row, col, 'X')
            move = (0, 1)
                
    elif dir == '<':
        if col != 0:
            if map[row][col-1] != '#':
                move = (0, -1)
                update_map(row, col-1, '<')
                update_map(row, col, 'X')
            else:
                update_map(row, col, '^')
        else:
            update_map(row, col, 'X')
            move = (0, -1)
                
    return move
    


map = []
row = col = 0
with open("day6-data.txt") as f:

    # Read the file and initialise the start pos
    i = 0
    for line in f.readlines():
        map.append(line.strip('\n'))
        if line.find('>') != -1:
            col = line.find('>')
            row = i
        elif line.find('<') != -1:
            col = line.find('<')
            row = i
        elif line.find('^') != -1:
            col = line.find('^')
            row = i
        elif line.find('v') != -1:
            col = line.find('v')
            row = i
        i += 1

print_map(map)

while row > -1 and row < len(map) and col > -1 and col < len(map[0]):
    move = get_move(row, col)
    row += move[0]
    col += move[1]

sum = 0 
for row in map:
    sum += row.count('X')

print("Day 6, part 1 = ", sum)

    
