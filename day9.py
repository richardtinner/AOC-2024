disk_map = ""
free_list = []
file_list = []

def expand_disk_map(dm):
    file = True
    id = 0
    ex_dm = ""
    disk_index = 0
    print("Expand Disk")
    for index, c in enumerate(dm):
        if file:
            for j in range(0, int(c)):
                ex_dm += str(id)
                file_list.append(id)
            id += 1
            disk_index += int(c)
        else:
            for j in range(0, int(c)):
                ex_dm += '.'
                file_list.append(-1)
            if int(c) != 0:
                free_list.append((disk_index, int(c)))
            
            disk_index += int(c)
            
        file = not file
        
    return 

def compress_disk():
    print("Compress Disk")
    x = 0
    while -1 in file_list:
        f = file_list.pop()
        if f != -1:
            try:
                i = file_list.index(-1)
                file_list[i] = f
            except ValueError:
                i = 0
        if x % 1000 == 0:
            print(x)
        x+=1
            

def sum_disk():
    print("Sum Disk")
    sum = 0
    for index, c in enumerate(file_list):
        sum += index * c

    return sum

        


with open("day9-data.txt") as f:
    disk_map = f.read()

expand_disk_map(disk_map)
compress_disk()
print("Day 9, part 1 = ", sum_disk())
