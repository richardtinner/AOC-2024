
move = {
    '^': (0,-1),
    '>': (1, 0),
    'v': (0,1),
    '<': (-1,0)
}

class grid:
    walls = set()
    boxes = set()
    spaces = set()

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def add_row(self, y, row):
        x = 0
        if y > self.height:
            self.height = y+1

        for c in row.strip('\n'):
            if c == '#':
                self.walls.add((x, y))
            elif c == '.':
                self.spaces.add((x,y))
            elif c == 'O':
                self.boxes.add((x,y))
            elif c == '@':
                self.x = x
                self.y = y
            x+=1

        self.width = x

    def slide(self, m, pos, new_pos):
        next_pos = (new_pos[0] + move[m][0], new_pos[1] + move[m][1])
         
        c = 1
        while next_pos in self.boxes:
            c+=1
            next_pos = (next_pos[0] + move[m][0], next_pos[1] + move[m][1])
        
        if next_pos in self.spaces:
            self.spaces.add(pos)
            self.spaces.remove(next_pos)
            self.boxes.remove(new_pos)
            self.x = new_pos[0]
            self.y = new_pos[1]

            box_pos = (new_pos[0] + c * move[m][0], new_pos[1] + c * move[m][1])
            self.boxes.add(box_pos)

        return
    
    def move(self, m):
        pos = (self.x, self.y)
        new_pos = (self.x + move[m][0], self.y + move[m][1])
        if new_pos in self.spaces:
            self.spaces.add(pos)
            self.spaces.remove(new_pos)
            self.x = new_pos[0]
            self.y = new_pos[1]
        elif new_pos in self.walls:
            pass
        elif new_pos in self.boxes:
            self.slide(m, pos, new_pos) 


    def print_grid(self):
        for y in range (0, self.height):
            for x in range (0, self.width):
                if (x,y) in self.walls:
                    print('#',end='')
                elif (x,y) in self.boxes:
                    print('O',end='')
                elif (x,y) in self.spaces:
                    print('.',end='')
                elif x == self.x and y == self.y:
                    print('@',end='')
            print()

        return
    
    def sum_all_boxes(self):
        sum = 0
        for box in self.boxes:
            sum += box[0]
            sum += box[1] * 100
        return sum

class grid2:
    walls = set()
    boxes1 = set()
    boxes2 = set()
    spaces = set()

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def add_row(self, y, row):
        x = 0
        if y > self.height:
            self.height = y+1

        for c in row.strip('\n'):
            if c == '#':
                self.walls.add((x, y))
                self.walls.add((x+1, y))
            elif c == '.':
                self.spaces.add((x,y))
                self.spaces.add((x+1,y))
            elif c == '#':
                self.boxes.add((x,y))
                self.boxes2.add((x+1,y))
            elif c == '@':
                self.x = x
                self.y = y
                self.spaces.add((x+1,y))
            x+=2

        self.width = x

    def slide(self, m, pos, new_pos):
        next_pos = (new_pos[0] + move[m][0], new_pos[1] + move[m][1])
         
        c = 1
        while next_pos in self.boxes:
            c+=1
            next_pos = (next_pos[0] + move[m][0], next_pos[1] + move[m][1])
        
        if next_pos in self.spaces:
            self.spaces.add(pos)
            self.spaces.remove(next_pos)
            self.boxes.remove(new_pos)
            self.x = new_pos[0]
            self.y = new_pos[1]

            box_pos = (new_pos[0] + c * move[m][0], new_pos[1] + c * move[m][1])
            self.boxes.add(box_pos)

        return
    
    def move(self, m):
        pos = (self.x, self.y)
        new_pos = (self.x + move[m][0], self.y + move[m][1])
        if new_pos in self.spaces:
            self.spaces.add(pos)
            self.spaces.remove(new_pos)
            self.x = new_pos[0]
            self.y = new_pos[1]
        elif new_pos in self.walls:
            pass
        elif new_pos in self.boxes:
            self.slide(m, pos, new_pos) 


    def print_grid(self):
        for y in range (0, self.height):
            for x in range (0, self.width):
                if (x,y) in self.walls:
                    print('#',end='')
                elif (x,y) in self.boxes1:
                    print('[',end='')
                elif (x,y) in self.boxes2:
                    print(']',end='')
                elif (x,y) in self.spaces:
                    print('.',end='')
                elif x == self.x and y == self.y:
                    print('@',end='')
            print()

        return
    
    def sum_all_boxes(self):
        sum = 0
        for box in self.boxes:
            sum += box[0]
            sum += box[1] * 100
        return sum
    

g = grid()
g2 = grid2()
moves = []

with open("day15-data.txt") as f:
   maze = True
   y = 0
   for line in f.readlines():
       if line == "\n":
           maze = False
           continue
       
       if maze:
           g.add_row(y, line)
           g2.add_row(y, line)
           y+=1
       else:
           moves += [c for c in line.strip('\n')]
   
   for m in moves:
       g.move(m)

   g.print_grid()

   print("Day15, part 1 = ", g.sum_all_boxes())

   g2.print_grid()


       
    
