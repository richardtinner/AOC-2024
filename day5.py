import re

po_rules_dict = {}
update_page_numbers = []
with open("day5-data.txt") as f:

    # Read the file
    po_rules = True
    for line in f.readlines():
        if line == "\n":
            po_rules = False
            continue

        if po_rules:
            data = re.findall("\d+", line)
            if int(data[0]) not in po_rules_dict:
                po_rules_dict[int(data[0])] = [int(data[1])]
            else:
                po_rules_dict[int(data[0])].append(int(data[1]))
        else:
            data = re.findall("\d+", line)
            update_page_numbers.append([int(pg) for pg in data])

# Part 1
total = 0
for update in update_page_numbers:
    ordered = True
    for i in range(len(update)-1, 0, -1):
        for j in range(0, i):
            if update[i] in po_rules_dict:
                if update[j] in po_rules_dict[update[i]]:
                    # update[j] must go after update[i]
                    ordered = False
                    break
        if not ordered:
            break
    
    if ordered:
        total += update[int((len(update)-1)/2)]
    
print("Day5, part 1 = ", total)


# Part 2
total = 0
for update in update_page_numbers:
    ordered = True
    incorrect = False
    i = len(update)-1
    while i > 0:
        for j in range(0, i):
            if update[i] in po_rules_dict:
                if update[j] in po_rules_dict[update[i]]:
                    # update[j] must go after update[i]
                    ordered = False
                    incorrect = True
                    break
        
        if ordered:
            i -= 1
        else:
            ordered = True
            pn = update[j]
            update.remove(pn)
            update.insert(i, pn)
    
    if incorrect:
        total += update[int((len(update)-1)/2)]
    
print("Day5, part 2 = ", total)

    



