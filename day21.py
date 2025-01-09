import networkx as nx
import matplotlib.pyplot as plt

numeric_keypad = {
    ('A', '0') : '<',
    ('A', '3') : '^',
    ('0', 'A') : '>',
    ('0', '2') : '^',
    ('1', '2') : '>',
    ('1', '4') : '^',
    ('2', '1') : '<',
    ('2', '0') : 'v',
    ('2', '3') : '>',
    ('2', '5') : '^',
    ('3', '2') : '<',
    ('3', 'A') : 'v',
    ('3', '6') : '^',
    ('4', '1') : 'v',
    ('4', '5') : '>',
    ('4', '7') : '^',
    ('5', '8') : '^',
    ('5', '4') : '<',
    ('5', '6') : '>',
    ('5', '2') : 'v',
    ('6', '5') : '<',
    ('6', '3') : 'v',
    ('6', '9') : '^',
    ('7', '4') : 'v',
    ('7', '8') : '>',
    ('8', '7') : '<',
    ('8', '5') : 'v',
    ('8', '9') : '>',
    ('9', '8') : '<',
    ('9', '6') : 'v'
}

direction_keypad = {
    ('A', '^') : [['<']],
    ('A', 'v') : [['v', '<'], ['<', 'v']],
    ('A', '>') : [['v']],
    ('A', '<') : [['<', 'v', '<'], ['v', '<', '<']],
    ('A', 'A') : [[]],

    ('^', 'A') : [['>']],
    ('^', 'v') : [['v']],
    ('^', '>') : [['>', 'v'], ['v', '>']],
    ('^', '<') : [['v', '<']],
    ('^', '^') : [[]],

    ('<', 'A') : [['>', '^', '>'], ['>', '>', '^']],
    ('<', 'v') : [['>']],
    ('<', '>') : [['>', '>']],
    ('<', '^') : [['>', '^']],
    ('<', '<') : [[]],

    ('v', 'A') : [['^', '>'], ['>', '^']],
    ('v', '^') : [['^']],
    ('v', '>') : [['>']],
    ('v', '<') : [['<']],
    ('v', 'v') : [[]],

    ('>', 'A') : [['^']],
    ('>', 'v') : [['<']],
    ('>', '^') : [['^', '<'], ['<', '^']],
    ('>', '<') : [['<', '<']],
    ('>', '>') : [[]]
}

def convert_numeric_keypad_paths_to_moves(paths: list):
    numeric_keypad_moves = []
    for path in paths:
        numeric_keypad_moves.append([numeric_keypad[(path[x], path[x+1])] for x in range(0, len(path)-1)])

    for moves in numeric_keypad_moves:
        moves.append('A')

    return numeric_keypad_moves

def print_sequences(sequences: list):
    for sequence in sequences:
        for c in sequence:
            print(c, end='')
        print()

with open("day21-data.txt") as file:
    codes = []
    for line in file.readlines():
        codes.append([c for c in line.strip('\n')])
    print(codes)

    G = nx.Graph()
    for n in numeric_keypad:
        G.add_edge(n[0], n[1])

    #nx.draw(G, with_labels=True)
    #plt.show()

    #keypad1_sequences = []
    total = 0
    for code in codes:
        print("=============")
        print(code)
       
        # First calculate paths from 'A' to the starting character
        # Don't try and merge this into the next loop as the list starts empty so the combination line returns 0
        paths = [path for path in nx.all_shortest_paths(G, 'A', code[0])]
        keypad1_sequences = convert_numeric_keypad_paths_to_moves(paths)

        # Next calculate the shortest route options for the code on the numeric keypad, convert to keypad1 directions and append to the 
        for n in range(0,len(code)-1):
            paths = [path for path in nx.all_shortest_paths(G, code[n], code[n+1])]
            moves = convert_numeric_keypad_paths_to_moves(paths)
            new_keypad1_sequences = [x + y for x in keypad1_sequences for y in moves]
            keypad1_sequences = new_keypad1_sequences
        
        print("direction pad 1 = ", len(keypad1_sequences))

        # Now convert into key presses for direction pad 2
        keypad2_all_sequences = []
        for sequence in keypad1_sequences:
            # First calculate paths from 'A to the starting direction and then press 'A'
            keypad2_sequences = direction_keypad[('A', sequence[0])]
            keypad2_sequences = [s + ['A'] for s in keypad2_sequences]

            # Next calculate the shortest route options for the rest of the code and press 'A' after each
            for i in range(0, len(sequence) - 1):
                moves = direction_keypad[(sequence[i], sequence[i+1])]
                if len(moves) > 0:
                    moves = [m + ['A'] for m in moves]
                else:
                    moves = [['A']]
                new_keypad2_sequences = [x + y for x in keypad2_sequences for y in moves]
                keypad2_sequences = new_keypad2_sequences
            keypad2_all_sequences = keypad2_all_sequences + keypad2_sequences

        print("direction pad 2 = ", len(keypad2_all_sequences))

        # Now convert into key presses for direction pad 3
        keypad3_all_sequences = []
        for sequence in keypad2_all_sequences:
            # First calculate paths from 'A to the starting direction and then press 'A'
            keypad3_sequences = direction_keypad[('A', sequence[0])]
            keypad3_sequences = [s + ['A'] for s in keypad3_sequences]

            # Next calculate the shortest route options for the rest of the code and press 'A' after each
            for i in range(0, len(sequence) - 1):
                moves = direction_keypad[(sequence[i], sequence[i+1])]
                if len(moves) > 0:
                    moves = [m + ['A'] for m in moves]
                else:
                    moves = [['A']]
                new_keypad3_sequences = [x + y for x in keypad3_sequences for y in moves]
                keypad3_sequences = new_keypad3_sequences
            keypad3_all_sequences = keypad3_all_sequences + keypad3_sequences

        print("direction pad 3 = ", len(keypad3_all_sequences))

        lengths = [len(sequence) for sequence in keypad3_all_sequences]
        sorted_lengths = sorted(lengths)
        shortest = sorted_lengths[0]
        total += shortest * int(code[0] + code[1] + code[2])
        print("shortest = ", shortest, "code = ", int(code[0] + code[1] + code[2]), "score = ", shortest * int(code[0] + code[1] + code[2]))

    print("Dat 21 part 1, total = ", total)

    
        


    



