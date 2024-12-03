import re

def multiply(m):
    nums = re.findall("\d+", m)
    return int(nums[0]) * int(nums[1])

# read the file into single string array
with open("day3-data.txt") as f:
    data = f.read()

# find all matches of mul(num1,num2) and multiply each pair
matches = re.findall("mul\(\d+,\d+\)", data)
sum = 0
for m in matches:
    sum += multiply(m)

print("Day 3, Part1 = ", sum)

