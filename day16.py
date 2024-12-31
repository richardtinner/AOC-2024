import heapq
import sys

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
g_lowest_cost = 127520
g_routes = []
g_cost_so_far = {}

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

    # return list of neighbours. If direction is set then do not return the neighbour which is in the direction you have came from
    # I.e do not allow backtracking
    def get_neighbours(self, node, direction = (-1,-1)):
        neighbours = []
        reverse_dir = (-1 * direction[0], -1 * direction[1])
        for dx,dy in directions:
            if self.rows[node[1] + dy][node[0] + dx] != '#' and (dx, dy) != reverse_dir:
                neighbours.append(((node[0] + dx,node[1] + dy), (dx, dy)))
        return neighbours
    
    def get_cost(self, current, next, direction):
        if next == (current[0] + direction[0], current[1] + direction[1]):
            return 1 # 1 square forward
        elif next == (current[0] - direction[0], current[1] - direction[1]):
            return 2001 # turn 180 degrees and 1 square forward.
        else:
            return 1001 # turn 90 degrees and 1 square forward

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

            for next, next_direction in self.get_neighbours(current, direction):
                new_cost = cost_so_far[current] + self.get_cost(current, next, direction)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    heapq.heappush(frontier, (new_cost, next, next_direction))
                    came_from[next] = current

        path = self.get_route(current, came_from)

        return cost_so_far[self.end], path
    
    def move(self, previous, current, direction, route, cost_so_far):
        global g_lowest_cost
        global g_routes
        global g_cost_so_far

        # Add the cost to get to this node
        if previous != (0, 0):
            cost_so_far += self.get_cost(previous, current, direction)
            direction = (current[0] - previous[0], current[1] - previous[1])
            # if we have ever been here before via a more expensive route then return
            if current in g_cost_so_far:
                if g_cost_so_far[current] < cost_so_far:
                    return
                elif g_cost_so_far[current] > cost_so_far:
                    g_cost_so_far[current] = cost_so_far
            else:
                g_cost_so_far[current] = cost_so_far
        
        # If we are at the end then return
        if current == self.end:
                # found solution
                if cost_so_far < g_lowest_cost:
                    g_lowest_cost = cost_so_far
                    g_routes = [route]
                elif cost_so_far == g_lowest_cost:
                    g_routes.append(route)
                
                #self.print_route(route)
                print("Cost = ", cost_so_far)
                return

        # Try moving to all neighbours
        for next, _ in self.get_neighbours(current, direction):
            if cost_so_far > g_lowest_cost:
                return
            if next not in route:
                self.move(current, next, direction, route + [next], cost_so_far)

        return
    
    def solve_part2(self):

        self.move((0,0), self.start, (1,0), [self.start], 0)

        return



with open("day16-data.txt") as f:
    g = grid()
    for line in f.readlines():
        g.add_row(line)
    
    cost, route = g.solve()
    g.print_route(route)
    print("Day 16 part 1, cost = ", cost)

    sys.setrecursionlimit(15000)
    g.solve_part2()
    print (len(g_routes))
    nodes = set()
    for r in g_routes:
        for n in r:
            nodes.add(n)
    print(len(nodes))

    
                


