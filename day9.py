import copy

disk_map = ""
free_list = []
file_list = []
file_list2 = []


def expand_disk_map(dm):
    file = True
    id = 0
    disk_index = 0
    print("Expand Disk")
    for index, c in enumerate(dm):
        if file:
            for j in range(0, int(c)):
                file_list.append(id)
            file_list2.append((disk_index, j+1, id))
            id += 1
            
        else:
            for j in range(0, int(c)):
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
        if x % 1000 == 0:
            print(x)
        x+=1
        f = file_list.pop()
        if f != -1:
            try:
                i = file_list.index(-1)
                file_list[i] = f
            except ValueError:
                i = 0
        


def compress_disk2():
    print("Compress Disk2")
    x = 0
    for f in reversed(file_list2):
        if x % 1000 == 0:
            print(x)
        x+=1


        found = False
        for index, s in enumerate(free_list):
            if s[0] > f[0]:
                break
            
            if s[1] >= f[1]:
                for i in range(s[0], s[0]+f[1]):
                    file_list[i] = f[2]

                for i in range(f[0], f[0]+f[1]):
                    file_list[i] = -1
                found = True
                break
        
        if found:
            free_list[index] = (s[0]+f[1], s[1]-f[1])




            

def sum_disk():
    print("Sum Disk")
    sum = 0
    for index, c in enumerate(file_list):
        if c != -1:
            sum += index * c

    return sum

        


with open("day9-data.txt") as f:
    disk_map = f.read()

expand_disk_map(disk_map)

# Part 1
original_file_list = copy.deepcopy(file_list)
compress_disk()
print("Day 9, part 1 = ", sum_disk())

# Part 2
file_list = copy.deepcopy(original_file_list)
print(len(file_list))
print(file_list)
compress_disk2()
print("Day 9, part 2 = ", sum_disk())

#print(file_list)
print(len(file_list))
