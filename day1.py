list1 = []
list2 = []

# Read the data
with open("day1-data.txt") as f:
    for line in f.readlines():
        data = line.strip('\n')
        data = data.split("   ")
        list1.append(int(data[0]))
        list2.append(int(data[1]))

# Sort the list
list1.sort()
list2.sort()

# Part 1: calculate the difference
diff = 0
i = 0
while i < len(list1):
    diff += abs(list1[i]-list2[i])
    i+=1

print(diff)

# Part 2: 
# 
# calculate how often each number appears in list 2
list2dict = {}
for n in list2:
    if n in list2dict:
        list2dict[n] += 1
    else:
        list2dict[n] = 1

# iterate through list 1 and calclaute the similarity score
similarity_score = 0
for n in list1:
    if n in list2dict:
        similarity_score += n * list2dict[n]

print(similarity_score)