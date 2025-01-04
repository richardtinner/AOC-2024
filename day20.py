import heapq
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Grid:
    rows = []
    walls = set()
    spaces = set()

    def __init__(self, filename):
        with open(filename) as f:
            # Read the file
            bytes_read = 0
            for y, line in enumerate(f.readlines()):
                self.rows.append([])
                for x, c in enumerate(line.strip('\n')):
                    self.rows[y].append(c)
                    if c == '#':
                        self.walls.add((x, y))
                    elif c == '.':
                        self.spaces.add((x,y))
                    elif c == 'S':
                        self.start = (x, y)
                        self.spaces.add((x,y))
                    elif c == 'E':
                        self.end = (x,y)
                        self.spaces.add((x,y))

    def print_grid(self, route = []):
        for y, row in enumerate(self.rows):
            for x, c in enumerate(row):
                print('O', end='') if (x,y) in route else print(c, end='')
            print()
        print("Start = ", self.start)
        print("End = ", self.end)

    def get_neighbours(self, node):
        neighbours = []
        for dx,dy in directions:
            if (node[0] + dx, node[1] + dy) not in self.walls:
                neighbours.append((node[0] + dx, node[1] + dy))
        return neighbours
    
    def get_route(self, current, came_from):
        path = []
        while current != self.start: 
            path.append(current)
            current = came_from[current]
        path.append(self.start) 
        path.reverse()
        return path
    
    def solve(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0
        

        while frontier:
            _, current = heapq.heappop(frontier)
            if current == self.end:
                break

            for next in self.get_neighbours(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    heapq.heappush(frontier, (new_cost, next))
                    came_from[next] = current

        path = self.get_route(current, came_from)

        if self.end in cost_so_far:
            path = self.get_route(current, came_from)
            return cost_so_far[self.end], path
        
        else:
            return -1, []
        
    def get_cheats(self):
        cheats = set()
        for w in self.walls:
            if w[0] == 0 or w[1] == 0 or w[0] == len(self.rows)-1 or w[1] == len(self.rows[0])-1:
                continue
            if ((w[0], w[1]+1) in self.spaces and (w[0], w[1]-1) in self.spaces) or \
                ((w[0]+1, w[1]) in self.spaces and (w[0]-1, w[1]) in self.spaces):
                cheats.add(w)
        return(cheats)

            
            
    def solve_with_cheats(self, time_saving = 100):
        # First solve without cheats to get baseline time
        base_t, _ = self.solve()
        print("base time = ", base_t)
        solutions = {}

        cheats = self.get_cheats()
        print("num cheats = ", len(cheats))
        c = 0
        for cheat in cheats:
            c+=1
            if c % 100 == 0:
                print(c)
            # apply cheat
            self.walls.remove(cheat)
            self.spaces.add(cheat)
            self.rows[cheat[1]][cheat[0]] = '.'

            t, _ = self.solve()
            if t <= base_t - time_saving:
                if base_t - t in solutions:
                    solutions[base_t-t].append(cheat)
                else:
                    solutions[base_t-t] = [cheat]


            # cancel cheat
            self.walls.add(cheat)
            self.spaces.remove(cheat)
            self.rows[cheat[1]][cheat[0]] = '#'

        total_sol = 0
        for k, v in sorted(solutions.items()):
            print(k, len(v))
            total_sol+=len(v)

        return total_sol


#g = Grid("day20-sample.txt")
#print("Part1 sample data: ", g.solve_with_cheats(0))

g = Grid("day20-data.txt")
print("Part1 real data: ", g.solve_with_cheats(100))


