towels = []
designs = []

def check_design(design):
    for t in towels:
        if design.startswith(t):
            if len(t) == len(design):
                return 1
            else:
                if check_design(design[len(t):]) == 1:
                    return 1
    
    return 0

with open("day19-data.txt") as f:
    lines = f.readlines()
    towels = [t.strip(' ') for t in lines[0].strip('\n').split(',')]
    designs = [d.strip('\n') for d in lines[2:]]
    print(towels)

    sum = 0
    for d in designs:
        print("Checking ", d, end=' ')
        if check_design(d) == 1:
            sum += 1
            print("found")
        else:
            print("impossible")
    
    print("Day 19 part 1 = ", sum)




