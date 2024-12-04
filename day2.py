reports = []

def check_report(r):
    asc = (r[1] - r[0]) > 0
    safe = True
    for i in range(len(r)-1):
        if 1 <= abs(r[i+1] - r[i]) <= 3:
            if ((r[i+1] - r[i]) > 0) == asc:
                continue
        safe = False
        break

    if safe:
        return -1
    else:
        return i



# Read the data
with open("day2-data.txt") as f:
    for line in f.readlines():
        data = line.strip('\n')
        data = data.split(" ")
        data = [int(numeric_string) for numeric_string in data]
        reports.append(data)



# Part 1 - Iterate over array
total_safe = 0
for r in reports:
    if check_report(r) == -1:
        total_safe += 1
    
print("Part 1, total safe = ", total_safe)

# Part 2 - Iterate over the array
total_safe = 0
for r in reports:
    i = check_report(r)
    if i == -1:
        total_safe += 1
    else:
        if i == len(r) - 2:
            total_safe += 1
        elif i == 0:
            r1 = r[1:]
            r2 = r[0:1] + r[2:]
            if check_report(r1) == -1 or check_report(r2) == -1:
                total_safe += 1

        else:
            r1 = r[0:i] + r[i+1:]
            r2 = r[0:i+1] + r[i+2:]
            if check_report(r1) == -1 or check_report(r2) == -1:
                total_safe += 1

print("Part 2, total safe = ", total_safe)

