
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
        if y + 1 > self.height:
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
    boxes = set()
    spaces = set()

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def add_row(self, y, row):
        x = 0
        if y + 1 > self.height:
            self.height = y+1

        for c in row.strip('\n'):
            if c == '#':
                self.walls.add((x, y))
                self.walls.add((x+1, y))
            elif c == '.':
                self.spaces.add((x,y))
                self.spaces.add((x+1,y))
            elif c == 'O':
                self.boxes.add((x,y))
            elif c == '@':
                self.x = x
                self.y = y
                self.spaces.add((x+1,y))
            x+=2

        self.width = x

        return
    
    def slide_left(self, m, pos):
        # determine how many boxes stacked together
        next_box = (pos[0]-2, pos[1])
        boxes = 0
        while next_box in self.boxes:
            boxes+=1
            next_box = (next_box[0]-2, next_box[1])
        
        # can only slide if last positon is a space
        if (next_box[0] + 1, next_box[1]) in self.spaces:
            self.x = pos[0] - 1
            self.spaces.add(pos)
            self.spaces.remove((next_box[0] + 1, next_box[1]))
            for b in range (1, boxes+1):
                self.boxes.remove((pos[0] - b * 2, pos[1]))
                self.boxes.add((pos[0] - b * 2 - 1, pos[1]))

        return
    
    def slide_right(self, m, pos):
        # determine how many boxes stacked together
        next_box = (pos[0]+1, pos[1])
        boxes = 0
        while next_box in self.boxes:
            boxes+=1
            next_box = (next_box[0]+2, next_box[1])
        
        # can only slide if last positon is a space
        if next_box in self.spaces:
            self.x = pos[0] + 1
            self.spaces.add(pos)
            self.spaces.remove(next_box)
            for b in range (0, boxes):
                self.boxes.remove((pos[0] + b * 2 + 1, pos[1]))
                self.boxes.add((pos[0] + b * 2 + 2, pos[1]))

        return
    
    def slide_vertical(self, m, pos, box):
        boxes_to_slide = set()
        boxes_to_slide.add(box)
        new_pos = (pos[0], pos[1] + move[m][1])
        can_slide = False

        while not can_slide:
            new_boxes_to_slide = set()
            for b in boxes_to_slide:
                # 2 positions abover the box to check
                next1 = (b[0], b[1] + move[m][1])
                next2 = (b[0] + 1, b[1] + move[m][1])
                next3 = (b[0] - 1, b[1] + move[m][1])
                
                # if either position is a wall we cannot slide any boxes
                if next1 in self.walls or next2 in self.walls:
                    return
                # if either position is a box add that to the boxes to slide. Won't be able to slide this round.
                if next1 not in boxes_to_slide and next1 in self.boxes:
                    new_boxes_to_slide.add(next1)
                if next2 not in boxes_to_slide and next2 in self.boxes:
                    new_boxes_to_slide.add(next2)
                if next3 not in boxes_to_slide and next3 in self.boxes:
                    new_boxes_to_slide.add(next3)
            
            # if new_boxes_to_slide is empty then we are good to slide
            if len(new_boxes_to_slide) == 0:
                can_slide = True
            else:
                boxes_to_slide |= new_boxes_to_slide

        if can_slide:
            # slide the boxes.
            # first remove the boxes
            for b in boxes_to_slide:
                self.boxes.remove(b)

            # then add the boxes in the new position
            for b in boxes_to_slide:
                self.boxes.add((b[0], b[1] + move[m][1]))
            
            # then remove any spaces that are now occupied by boxes
            for b in boxes_to_slide:
                if (b[0], b[1] + move[m][1]) in self.spaces:
                    self.spaces.remove((b[0], b[1] + move[m][1]))
                if (b[0] + 1, b[1] + move[m][1]) in self.spaces:
                    self.spaces.remove((b[0] + 1, b[1] + move[m][1]))

            # Now add any new spaces created by sliding the boxes
            for b in boxes_to_slide:
                if not ((b in self.boxes) or (b[0]-1, b[1]) in self.boxes):
                    self.spaces.add(b)
                if not((b[0]+1, b[1]) in self.boxes or (b[0], b[1]) in self.boxes):
                    self.spaces.add((b[0]+1, b[1]))

            # Finally move the current position (no change to self.x)
            self.y = new_pos[1]
            self.spaces.add(pos)
            self.spaces.remove(new_pos)



        return

    def slide(self, m, pos, box = (-1,-1)):
        if m == '<' :
            self.slide_left(m, pos)
        elif m == '>':
            self.slide_right(m, pos)
        elif m == '^':
            self.slide_vertical(m, pos, box)
        else:
            self.slide_vertical(m, pos, box)

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
        else:
            in_box, box = self.new_position_in_box(pos, m)
            if in_box:
                self.slide(m, pos, box)

    def new_position_in_box(self, pos, m):
        if (m == '>' and (pos[0] + 1, pos[1]) in self.boxes):
            return True, (pos[0] + 1, pos[1])
        elif(m == '<' and (pos[0] - 2, pos[1]) in self.boxes):
            return True, (pos[0] - 2, pos[1])
        elif (m == '^' and (pos[0], pos[1] - 1) in self.boxes):
            return True, (pos[0], pos[1] - 1)
        elif (m == '^' and (pos[0] - 1, pos[1] - 1) in self.boxes):
            return True, (pos[0] - 1, pos[1] - 1)
        elif (m == 'v' and (pos[0], pos[1] + 1) in self.boxes):
            return True, (pos[0], pos[1] + 1)
        elif (m == 'v' and (pos[0] - 1, pos[1] + 1) in self.boxes):
            return True, (pos[0] - 1, pos[1] + 1)
        
        return False, (-1,-1)
    
        

    def print_grid(self):
        for y in range (0, self.height):
            for x in range (0, self.width):
                if (x,y) in self.walls:
                    print('#',end='')
                elif (x,y) in self.boxes:
                    print('[',end='')
                elif (x-1,y) in self.boxes:
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

   print("Initial Grid")
   g2.print_grid()
   print(len(g2.spaces))
   for m in moves:
       g2.move(m)
       #print("Grid after ", m)
       #g2.print_grid()
       #print(len(g2.spaces))
       #print()
    
   print("Final Grid")
   g2.print_grid()
   print(len(g2.spaces))

   print("Day15, part 2 = ", g2.sum_all_boxes())

       
    
