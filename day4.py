import re

ws = []
t_ws= []

def count_diag2(bld, brd):
    count = 0   
    if (bld == "MAS" or bld == "SAM") and (brd == "MAS" or brd == "SAM"):
            count = 1

    return count

def count_diag(trd,tld,brd,bld):
    count = 0
    
    if trd == "XMAS":
        count += 1
    if tld == "XMAS":
        count += 1
    if brd == "XMAS":
        count += 1
    if bld == "XMAS":
        count += 1

    return count


# read the file into single string array
with open("day4-data.txt") as f:
    for line in f.readlines():
        data = line.strip('\n')
        ws.append(data)

t_ws = [''.join(s) for s in zip(*ws)]
count = 0

# Part 1
# count horizontals
for r in ws:
    count += r.count("XMAS")
    count += r.count("SAMX")

# count verticals
for r in t_ws:
    count += r.count("XMAS")
    count += r.count("SAMX")

# count the diagonals
# i is horizontal index, j is vertical index
for i in range(0, len(ws[0])):
    for j in range(0, len(ws[0])):
        # This is a valid starting character
        if ws[i][j] != 'X':
            continue
        # build diagonal strings
        tld = trd = bld = brd = ""
        if j < len(ws[0]) - 3 and i > 2:
            trd = ws[i][j] + ws[i-1][j+1] + ws[i-2][j+2] + ws[i-3][j+3]
        if j > 2 and i > 2:
            tld = ws[i][j] + ws[i-1][j-1] + ws[i-2][j-2] + ws[i-3][j-3]
        if j < len(ws[0]) - 3 and i < len(ws[0]) - 3:
            brd = ws[i][j] + ws[i+1][j+1] + ws[i+2][j+2] + ws[i+3][j+3]
        if j > 2 and i < len(ws[0]) - 3:
            bld = ws[i][j] + ws[i+1][j-1] + ws[i+2][j-2] + ws[i+3][j-3]

        count += count_diag(trd,tld,brd,bld)


print("Day4 part 1, count = ", count)

# Part 2
count = 0
for i in range(1, len(ws[0])-1):

    for j in range(1, len(ws[0])-1):
        # This is a valid starting character
        if ws[i][j] != 'A':
            continue

        # build diagonal strings
        tld = trd = bld = brd = ""
        bld = ws[i+1][j-1] + ws[i][j] + ws[i-1][j+1]
        brd = ws[i+1][j+1] + ws[i][j] + ws[i-1][j-1]

        count += count_diag2(bld, brd)


print("Day4 part 2, count = ", count)


