import re

def multiply(m):
    nums = re.findall("\d+", m)
    return int(nums[0]) * int(nums[1])

def find_nearest_small_value(key, sorted_li):
    for i in sorted_li:
        if i <= key:
            return i
    return 0

# read the file into single string array
with open("day3-data.txt") as f:
    data = f.read()

# Part 1 find all matches of mul(num1,num2) and multiply each pair
matches = re.findall("mul\(\d+,\d+\)", data)
sum = 0
for m in matches:
    sum += multiply(m)

print("Day 3, Part1 = ", sum)

# Part 2 Need index of each match
m_i = []
m_dict = {}
for m in matches:
    m_i.append(data.find(m))
    m_dict[m_i[-1]] = m

do_i = [0] + [d.start() for d in re.finditer('do\(\)', data)]
do_i.sort(reverse=True)
dont_i = [d.start() for d in re.finditer('don\'t\(\)', data)]
dont_i.sort(reverse=True)

print(do_i)
print(dont_i)

# Iterate of the dictionary and look up previous do or don't
sum = 0
for key, m in m_dict.items():
    prev_do = find_nearest_small_value(key, do_i)
    prev_dont = find_nearest_small_value(key, dont_i)
    if prev_do >= prev_dont:
        sum += multiply(m)


print("Day 3, Part2 = ", sum)



