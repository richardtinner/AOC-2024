from collections import deque

inp = []
with open('day12-data.txt', 'r') as f:
  for line in f:
    inp.append(list(line.strip()))

# print(inp)
num_rows = len(inp)
num_cols = len(inp[0])

def in_bounds(rc):
  r, c = rc
  return (0 <= r < num_rows) and (0 <= c < num_cols)

def get_plant(rc):
  r, c = rc
  return inp[r][c]

def get_neighbors(rc):
  r, c = rc
  neighbors = []
  ds = [(-1, 0), (0, 1), (1, 0), (0, -1)] # NESW
  for (dr, dc) in ds:
    neighbors.append((r + dr, c + dc))
  return [n for n in neighbors if in_bounds(n)]

def get_plant_neighbors(rc):
  neighbors = get_neighbors(rc)
  return [n for n in neighbors if get_plant(n)==get_plant(rc)]

# BFS
def get_region(rc):
  visited = set()
  region = set()
  queue = deque([rc])
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      # visit node
      region.add(node)
      # add all unvisited neighbors to the queue
      neighbors = get_plant_neighbors(node)
      unvisited_neighbors = [n for n in neighbors if n not in visited]
      # print(f'At node {node}, ns: {neighbors}, unvisited: {unvisited_neighbors}')
      queue.extend(unvisited_neighbors)
  return region

def calc_perimeter(region):
  perimeter = 0
  for rc in region:
    plant = get_plant(rc)
    neighbors = get_plant_neighbors(rc)
    # Boundary adds to perimeter
    perimeter += 4 - len(neighbors)
    
  return perimeter

regions = []
visited = set()
for r in range(num_rows):
  for c in range(num_cols):
    rc = (r, c)
    if rc not in visited:
      region = get_region(rc)
      visited |= region
      regions.append(region)

# print(regions)

total_price = 0
for region in regions:
  plant = get_plant(next(iter(region)))
  area = len(region)
  perimeter = calc_perimeter(region)
  price = area * perimeter
  total_price += price
  # print(f'{plant} (area: {area}, perimeter: {perimeter}): {region}')

print(total_price)