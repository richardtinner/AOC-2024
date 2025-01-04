import heapq
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Grid:
    rows = []
    walls = set()
    spaces = set()

    def __init__(self, filename):
        with open(filename) as f:
            # Read the file
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
            return cost_so_far[self.end], path, cost_so_far
        
        else:
            return -1, [], []
            
    def get_shortcuts(self, node, max = 2):
        shortcuts = []
        for x in range(node[0] - max, node[0] + max + 1):
            for y in range(node[1] - max, node[1] + max + 1):
                if 0 <= x <= len(self.rows[0]) and 0 <= y <= len(self.rows):
                    if self.get_taxi_distance(node, (x,y)) <= max:
                        if (x, y) in self.spaces:
                            shortcuts.append((x, y))
        return shortcuts
    
    def get_taxi_distance(self, nodeA, nodeB):
        dx = abs(nodeA[0] - nodeB[0])
        dy = abs(nodeA[1] - nodeB[1])
        return dx + dy
    
    def solve_with_cheats(self, max_cheat_time, target_time_saving = 0):
        # first solve the maze
        base_t, route, cost_so_far = self.solve()
        print("base time = ", base_t)
        solutions = {}

        # iterate through the solution and see if there is a 2 space jump from any position that will save time
        for node in route:
            for jump_to in self.get_shortcuts(node, max_cheat_time):
                if cost_so_far[jump_to] > cost_so_far[node]: # only jump forward in route
                    time_saving = cost_so_far[jump_to] - cost_so_far[node] - self.get_taxi_distance(node, jump_to)
                    if time_saving >= target_time_saving: # jump has saved time
                        route_time = cost_so_far[self.end] - (cost_so_far[jump_to] - cost_so_far[node] + 2)
                        if time_saving in solutions:
                            solutions[time_saving].append(jump_to)
                        else:
                            solutions[time_saving] = [jump_to]
        
        total_sol = 0
        for k, v in sorted(solutions.items()):
            #print(k, len(v))
            total_sol+=len(v)

        return total_sol

#g = Grid("day20-sample.txt")
#print("Part1 sample data: ", g.solve_with_cheats(2, 0))

#g = Grid("day20-data.txt")
#print("Part1 real data: ", g.solve_with_cheats(2, 100))

#g = Grid("day20-sample.txt")
#print("Part2 sample data: ", g.solve_with_cheats(20, 0))

g = Grid("day20-data.txt")
print("Part1 real data: ", g.solve_with_cheats(20, 100))


