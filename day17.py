import itertools

def get_combo_operand(lo, registerA, registerB, registerC):
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

def run_program(registerA, registerB, registerC, program):
    ptr = 0

    while ptr < len(program):
        instr = program[ptr]
        operand = program[ptr + 1]
        combo_operand = get_combo_operand(operand, registerA, registerB, registerC)
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

    print()
    return 


with open("day17-data.txt") as f:
    # Read the file
    lines = f.readlines()
    registerA = int(lines[0].split(':')[1].strip('\n'))
    registerB = int(lines[1].split(':')[1].strip('\n'))
    registerC = int(lines[2].split(':')[1].strip('\n'))
    program = [int(c) for c in lines[4].split(':')[1].split(',')]
    
    # Solve part 1
    print("Day17 part 1")
    print("Program = ", program)
    print("Solution = ", end ='')

    run_program(registerA, registerB, registerC, program)
    
    # Part 2 
    sa = [0o7777777777777777, 0o1000000000000000, 0o777777777777777]
    for a in sa:
        print(a, oct(a))
        run_program(a, registerB, registerC, program)

    print(0o7777777777777777 - 0o1000000000000000)


    
