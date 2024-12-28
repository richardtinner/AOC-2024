import copy

class robot:
    def __init__(self, x, y, vx, vy, w, h):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h

    def move(self):
       self.x = (self.x + self.vx) % self.w
       self.y = (self.y + self.vy) % self.h
       c = 10

    def get_quadrant(self):
        if self.x < (self.w - 1) / 2:
           if self.y < (self.h - 1) / 2:
              return 0
           elif self.y > (self.h - 1) / 2:
              return 2
        elif self.x > (self.w - 1) / 2:
           if self.y < (self.h - 1) / 2:
              return 1
           elif self.y > (self.h - 1) / 2:
              return 3
        return -1
    
    def __str__(self):
       return f"p = ({self.x}, {self.y}) v = ({self.vx}, {self.vy})"

class Grid:
   p_dict = {}
   p_set = set()
   
   def __init__(self, robots):
      self.p_dict = {}
      self.p_set = set()
      for r in robots:
         self.p_set.add((r.x, r.y))
         if r.y in self.p_dict:
            self.p_dict[r.y].append(r.x)
         else:
            self.p_dict[r.y] = [r.x]
    
   def print_grid(self):
      for i in range (0, 103):
         for j in range(0, 101):
            if (j,i) in self.p_set:
               print('.', end='')
            else:
               print(' ', end='')
         print()
      return
   
   def check_symmetry(self):
    if len(self.p_set) > 497:
       print(len(self.p_set))
    symmetry = 0
    for p in self.p_set:
       if (100-p[0], p[1]) in self.p_set:
          #print(p, (100-p[0], p[1]))
          symmetry+=1
    return symmetry

    
    

robots = []
width = 101
height = 103
with open("day14-data.txt") as f:
   for line in f.readlines():
      x = int(line.split()[0].split('=')[1].split(',')[0])
      y = int(line.split()[0].split('=')[1].split(',')[1])
      vx = int(line.split()[1].split('=')[1].split(',')[0])
      vy = int(line.split()[1].split('=')[1].split(',')[1])
      robots.append(robot(x,y,vx,vy,width,height))

for n in range (0, 101):
    for r in robots:
        r.move()

quadrants = [0, 0, 0, 0]
for r in robots:
   q = r.get_quadrant()
   if q != -1:
      quadrants[q] += 1

print("Day 14 part 1:", quadrants, quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

max_sym = 0
max_n = 0
for n in range (0, 100000):
    
    for r in robots:
        r.move()

    g = Grid(robots)

    if len(g.p_set) == 500:
       g.print_grid()
       break



print("Day 14 part 2, seconds = ", n+1)