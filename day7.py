import re
import itertools

def generate_permutations(ops, n):
    # Generate all permutations of length n with elements 0 and 1
    return list(itertools.product(ops, repeat=n))

def validate(t, perms):
    
    ret = 0
    print('.', end='.')
    for p in perms:
        total = t[1][0]
        for i in range(0, len(p)):
            if p[i] == '+':
                total += t[1][i+1]
            elif p[i] == '*':
                total *= t[1][i+1]
            elif p[i] == '|':
                str_total = str(total) + str(t[1][i+1])
                total = int(str_total)
        
        if total == t[0]:
            print(t[0], end='.')
            ret = t[0]
            break


    return ret

test_values = []

with open("day7-data.txt") as f:

    # Read the file and initialise the start pos
    for line in f.readlines():
        data = re.split(':', line)
        test_values.append((int(data[0]), [int(v) for v in re.split(' ', data[1].strip('\n')[1:])]))
    
# Part 1
sum = 0
for t in test_values:
    permutations = generate_permutations(['+', '*'], len(t[1])-1)
    sum += validate(t, permutations)

print("")
print("Day7, part1 = ", sum)

# Part 2
sum = 0
for t in test_values:
    permutations = generate_permutations(['+', '*', '|'], len(t[1])-1)
    sum += validate(t, permutations)

print("")
print("Day7, part2 = ", sum)
