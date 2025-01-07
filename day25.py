locks = []
keys = []
with open("day25-data.txt") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 8):
        schematic = [line.strip('\n') for line in lines[i+1:i+6]]
        schematic_transposed = [[schematic[j][i] for j in range(len(schematic))] for i in range(len(schematic[0]))]
        pins = [a.count('#') for a in schematic_transposed]
        if (lines[i] == "#####\n"):
            locks.append(pins) # lock
        elif lines[i] == ".....\n":
            keys.append(pins) #key
 
    sum  = 0
    for lock in locks:
        for key in keys:
            test = [lock[i] + key[i] for i in range(0, len(lock))]
            if max(test) < 6:
                sum += 1
 
    print("Day 25 part 1, sum =", sum)