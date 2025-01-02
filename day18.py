import heapq
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Grid:
    size = 70
    start = (0,0)
    end = (size, size)
    bytes = []
    corrupt_bytes = []

    def __init__(self, filename, num_bytes):
        with open(filename) as f:
            # Read the file
            bytes_read = 0
            for line in f.readlines():
                self.bytes.append((int(line.strip('\n').split(',')[0]), int(line.strip('\n').split(',')[1])))
                if bytes_read < num_bytes:
                    self.corrupt_bytes.append((int(line.strip('\n').split(',')[0]), int(line.strip('\n').split(',')[1])))
                bytes_read+=1

    def set_corrupt(self, num_bytes):
        self.corrupt_bytes = []
        self.corrupt_bytes = self.bytes[:num_bytes]

    def print_grid(self, route = []):
        for y in range(0, self.size + 1):
            for x in range(0, self.size + 1):
                print('O', end='') if (x,y) in route else print('#', end='') if (x,y) in self.corrupt_bytes else print('.', end='')
            print()

    def get_neighbours(self, node):
        neighbours = []
        for dx,dy in directions:
            if (node[0] + dx, node[1] + dy) not in self.corrupt_bytes:
                if 0 <= node[0] + dx <= self.size and 0 <= node[1] + dy <= self.size:
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
        direction = (1, 0)
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



g = Grid("day18-data.txt", 1024)
cost, route = g.solve()
g.print_grid(route)
print("Day 18 part 1, steps = ", cost)

for i in range (2985, len(g.bytes)):
    g.set_corrupt(i)
    cost, route = g.solve()
    if cost == -1:
        print("Day 18 part 2, ", i, g.bytes[i-1])
        break




