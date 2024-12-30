import heapq

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class grid:
    rows_to_print = []
    rows = []

    def __init__(self):
        self.height = 0
        self.width  = 0
        self.visited = {}

    def add_row(self, row):
        row_to_add = []
        for x in range(0, len(row)):
            row_to_add.append(row[x])
            if row[x] == 'E':
                self.end = (x, len(self.rows))
            elif row[x] == 'S':
                self.start = (x, len(self.rows))


        self.rows.append(row_to_add)
        self.rows_to_print.append(row.strip('\n'))
        self.height = len(self.rows)
        self.width = len(row)
    
    def get_pos(self, pos):
        return(self.rows[pos[1]][pos[0]])
    
    def print_grid(self):
        for y in range (0, self.height):
            for x in range (0, self.width):
                if (x, y) in self.visited:
                    print('*', end='')
                else:
                    print(self.rows[y][x], end='')
            print()

    def print_route(self, route):
        for y in range (0, self.height):
            for x in range (0, self.width):
                if (x, y) in route:
                    print('*', end='')
                else:
                    print(self.rows[y][x], end='')
            print()


        print("width = ", self.width, ", height = ", self.height)
        print("E = ", self.end)
        print("S = ", self.start)

    def get_neighbours(self, node):
        neighbours = []
        for dx,dy in directions:
            if self.rows[node[1] + dy][node[0] + dx] != '#':
                neighbours.append(((node[0] + dx,node[1] + dy), (dx, dy)))
        return neighbours
    
    def get_cost(self, current, next, direction):
        if next == (current[0] + direction[0], current[1] + direction[1]):
            return 1 # 1 square forward
        elif next == (current[0] - direction[0], current[1] - direction[1]):
            return 2001 # turn 180 degrees and 1 square forward. should never happen
        else:
            return 1001 # turn 90 degrees and 1 square forward


    def solve(self):
        frontier = []
        direction = (1, 0)
        heapq.heappush(frontier, (0, self.start, direction))
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0
        

        while frontier:
            _, current, direction = heapq.heappop(frontier)
            if current == self.end:
                break

            for next, next_direction in self.get_neighbours(current):
                new_cost = cost_so_far[current] + self.get_cost(current, next, direction)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    heapq.heappush(frontier, (new_cost, next, next_direction))
                    came_from[next] = current

        path = []
        while current != self.start: 
            path.append(current)
            current = came_from[current]
        path.append(self.start) 
        path.reverse()

        return cost_so_far[self.end], path


with open("day16-data.txt") as f:
    g = grid()
    for line in f.readlines():
        g.add_row(line)
    
    cost, route = g.solve()
    g.print_route(route)
    print("Day 16 part 1, cost = ", cost)

    
                


