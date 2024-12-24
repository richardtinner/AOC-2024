wires = {}
gates = []

with open("day24-data.txt") as f:

    initial = True
    for line in f.readlines():
        if line == "\n":
            initial = False
            continue
        
        if initial:
            wires[line.split()[0].strip(':')] = int(line.split()[1])
        else:
            gate = line.strip('\n').split()
            gates.append([gate[0], gate[1], gate[2], gate[4], False])

    for gate in gates:
        if gate[0] not in wires:
            wires[gate[0]] = -1
        if gate[2] not in wires:
            wires[gate[2]] = -1

    all_done = False
    while not all_done:
        print('*', end='')
        all_done = True
        for gate in gates:
            if wires[gate[0]] != -1 and wires[gate[2]] != -1 and gate[4] == False:
                if gate[1] == "AND":
                    wires[gate[3]] = 1 if wires[gate[0]] + wires[gate[2]] == 2 else 0
                elif gate[1] == "OR":
                    wires[gate[3]] = 1 if wires[gate[0]] + wires[gate[2]] >= 1 else 0
                else:
                    wires[gate[3]] = 1 if wires[gate[0]] != wires[gate[2]] else 0
                gate[4] = True
                print('.', end='')
            elif gate[4] == False:
                all_done = False
        print()
            
#print(sorted(wires.items()))
#print(gates)

output = {}
for key, val in wires.items():
    if key[0] == 'z':
        output[key] = val

sorted_output = dict(sorted(output.items()))
power = 0
dec = 0
for key, val in sorted_output.items():
    print(key, val)
    dec += val * (2**power)
    power += 1

print(dec)
