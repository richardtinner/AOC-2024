registerA = 0
registerB = 0
registerC = 0
program = []
ptr = 0

def get_combo_operand(lo):
    co = lo
    if lo == 4:
        co = registerA
    elif lo == 5:
        co = registerB
    elif lo == 6:
        co = registerC
    elif lo == 7:
        # won't happen in a valid program - we may hit this, but in places that the combo operand is not used.
        pass

    return co

def process_instr(ptr):
    global registerA
    global registerB
    global registerC
    instr = program[ptr]
    operand = program[ptr + 1]
    combo_operand = get_combo_operand(operand)
    

    ptr += 2
    if instr == 0:
        registerA = int(registerA / 2 ** combo_operand)
    elif instr == 1:
        registerB = registerB ^ operand
    elif instr == 2:
        registerB = combo_operand % 8
    elif instr == 3:
        if registerA != 0:
            ptr = operand
    elif instr == 4:
        registerB = registerB ^ registerC
    elif instr == 5:
        print(combo_operand % 8, end = '')
        print(',', end='')
    elif instr == 6:
        registerB = int(registerA / 2 ** combo_operand)
    elif instr == 7:
        registerC = int(registerA / 2 ** combo_operand)

    return ptr

with open("day17-data.txt") as f:
    lines = f.readlines()
    registerA = int(lines[0].split(':')[1].strip('\n'))
    registerB = int(lines[1].split(':')[1].strip('\n'))
    registerC = int(lines[2].split(':')[1].strip('\n'))
    program = [int(c) for c in lines[4].split(':')[1].split(',')]
    print(program)

    while ptr < len(program):
        ptr = process_instr(ptr)
    
    print()
    
