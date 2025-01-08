import networkx as nx
import matplotlib.pyplot as plt

numeric_keypad = {
    ('A', '0') : '<',
    ('A', '3') : '^',
    ('0', 'A') : '>',
    ('0', '2') : '^',
    ('1', '2') : 'v',
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

def convert_numeric_keypad_paths_to_moves(paths: list):
    numeric_keypad_moves = []
    for path in paths:
        numeric_keypad_moves.append([numeric_keypad[(path[x], path[x+1])] for x in range(0, len(path)-1)])

    for moves in numeric_keypad_moves:
        moves.append('A')

    return numeric_keypad_moves

def print_moves(moves: list):
    for move in moves:
        for m in move:
            print(m, end='')
        print()

with open("day21-sample.txt") as file:
    codes = []
    for line in file.readlines():
        codes.append([c for c in 'A' + line.strip('\n')])
    print(codes)

    G = nx.Graph()
    for n in numeric_keypad:
        G.add_edge(n[0], n[1])

    #nx.draw(G, with_labels=True)
    #plt.show()

    numeric_keypad_moves = []
    for code in codes:
        print("=============")
        print(code)
       
        paths = [path for path in nx.all_shortest_paths(G, code[0], code[1])]
        numeric_keypad_moves = convert_numeric_keypad_paths_to_moves(paths)

        # First calculate the shortest route options for the code on the numeric keypad and convert to directions
        for n in range(1,len(code)-1):
            paths = [path for path in nx.all_shortest_paths(G, code[n], code[n+1])]
            moves = convert_numeric_keypad_paths_to_moves(paths)
            new_numeric_keypad_moves = [x + y for x in numeric_keypad_moves for y in moves]
            numeric_keypad_moves = new_numeric_keypad_moves

    print_moves(numeric_keypad_moves)
        


    



