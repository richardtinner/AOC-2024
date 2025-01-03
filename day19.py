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

    
def numMakes(design, made):
    if len(design) == 0:
        return 1
    if design in made:
        return made[design]
    
    numMade = 0
    for searchTo in range(0,len(design)):
        curr = design[0:searchTo + 1]
        if curr in towels:
            numMade += numMakes(design[searchTo + 1:],made)
 
    made[design] = numMade
    return numMade
 

with open("day19-data.txt") as f:
    lines = f.readlines()
    towels = [t.strip(' ') for t in lines[0].strip('\n').split(',')]
    designs = [d.strip('\n') for d in lines[2:]]

sum = 0
for d in designs:
    sum += check_design(d)
print("Day 19 part 1 = ", sum)

count = 0
made = {}
for d in designs:
    count += numMakes(d,made)

print("Day 19 part 2 = ", count)
        




