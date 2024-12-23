import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("day23-data.txt") as f:

    for line in f.readlines():
        edge = line.strip('\n').split('-')
        G.add_edge(edge[0], edge[1])
    
    print("num edges = ", G.number_of_edges(), "num nodes = ", G.number_of_nodes())
    #nx.draw(G)
    #plt.show()

    cycles = nx.simple_cycles(G, 3)
    
    count = 0
    found = []
    for c in cycles:
        for node in c:
            if node[0] == 't':
                count += 1
                found.append(c)
                break
    
    print("day 23, part 1 = ", count)

    cycles2 = nx.find_cliques(G)
    largest_cc = max(cycles2, key=len)


    print("day 23, part 2 = ", end='') 
    first = True
    for node in sorted(largest_cc):
        if not first:
            print(",", end='')
        print(node, end='')
        first = False

    print()


        
    

    
