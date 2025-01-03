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

def check_design2(design, sum):
    for t in towels:
        if design.startswith(t):
            if len(t) == len(design):
                return sum+1
            else:
                sum = check_design2(design[len(t):], sum)

    return sum

with open("day19-data.txt") as f:
    lines = f.readlines()
    towels = [t.strip(' ') for t in lines[0].strip('\n').split(',')]
    designs = [d.strip('\n') for d in lines[2:]]

    sum = 0
    for d in designs:
        sum += check_design(d)
    print("Day 19 part 1 = ", sum)
    
    sum = 0
    for d in designs:
        sum +=  check_design2(d, 0)
        
    print("Day 19 part 2 = ", sum)




