
machines = []

class machine:
    def __init__(self, a, b, p):
        self.ax = a[0]
        self.ay = a[1]
        self.bx = b[0]
        self.by = b[1]
        self.px = p[0]
        self.py = p[1]

    def __str__(self):  
        return f"Button A: ({self.ax}, {self.ay}) Button B: ({self.bx}, {self.by}) Prize: ({self.px}, {self.py})"
        


with open("day13-data.txt") as f:

    # Read the file, initialise the map and find the trailheads
    line = f.readline()
    while line:
        if line == '\n':
            line = f.readline()
        (xa, ya) = int(line.split("+")[1].split(',')[0]),  int(line.split("+")[2].strip('\n'))
        line = f.readline()
        (xb, yb) = int(line.split("+")[1].split(',')[0]),  int(line.split("+")[2].strip('\n'))
        line = f.readline()
        (x, y) = int(line.split("=")[1].split(',')[0]),  int(line.split("=")[2].strip('\n'))
        machines.append(machine((xa, ya), (xb, yb), (x,y)))
        line = f.readline()


# Part 1
total = 0
for m in machines:
    b = (m.px * m.ay - m.ax * m.py) / (m.bx * m.ay - m.ax * m.by)
    a = (m.py - m.by * b) / m.ay
    if b - int(b) == 0 and a - int(a) == 0:
        total += 3*int(a) + int(b)

print("Day 13 part 1 = ", total)

# Part 2
total = 0
for m in machines:
    b = ((10000000000000 + m.px) * m.ay - m.ax * (10000000000000 + m.py)) / (m.bx * m.ay - m.ax * m.by)
    a = ((10000000000000 + m.py) - m.by * b) / m.ay
    if b - int(b) == 0 and a - int(a) == 0:
        total += 3*int(a) + int(b)

print("Day 13 part 2 = ", total)





