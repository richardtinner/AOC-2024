from time import time

start = time()

with open("day9-data.txt") as f:
    data = f.read()

    cells = []
    datas = []
    frees = []
    cum_pos = 0

    for i, d in enumerate(data, 1):
        cells += [i//2+1 if i%2 else 0, ] * int(d)

        if i % 2:
            # array of [value, size, position] triplets
            datas.append([i//2+1, int(d), cum_pos])
        else:
            # need to update size and position of frees so these can't be tuples
            frees.append([0, int(d), cum_pos])

        cum_pos += int(d)

# print(cells)
# print(datas)
# print(frees)

def solve_p1(cells):
    total = 0

    start = 0
    end = len(cells) - 1
    while start <= end:
        if cells[start]:
            total += (cells[start] - 1) * start
        else:
            while not cells[end]:
                end -= 1
            total += (cells[end] - 1) * start
            end -= 1
        start += 1

    return total

def solve_p2(cells, datas, frees):
    for data in reversed(datas):

        # print("".join([str(c-1) if c else "." for c in cells]))

        for free_i in range(len(frees)):
            # data doesn't have a free before it, break loop
            if frees[free_i][2] > data[2]:
                break

            if frees[free_i][1] >= data[1]:
                # set values in cell list
                for i in range(data[1]):
                    cells[frees[free_i][2] + i] = data[0]
                    cells[data[2] + i] = 0

                # update free size and position
                frees[free_i][1] -= data[1]
                frees[free_i][2] += data[1]

                break

    total = sum([max(v-1, 0) * i for i, v in enumerate(cells)])
    return total

p1_total = solve_p1(cells)
p2_total = solve_p2(cells, datas, frees)

end = time()

print(f"Part 1 Solution: { p1_total }")
print(f"Part 2 Solution: { p2_total }")
print(f"Total time: { end - start }")