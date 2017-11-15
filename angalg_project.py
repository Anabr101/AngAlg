#imports
import sys
from itertools import permutations
#install via pip 
import networkx as nx


#read file from command line argument and parse into Directed Graph 
G = nx.DiGraph()
with open(sys.argv[1], "r") as file:
        for line in file:
        	inputList = line.split()
        	print(inputList)
        	G.add_edge(inputList[1], inputList[2], weight=int(inputList[3]))

#print out Nodes and Edges
print(G.nodes())
print(G.edges())

#Enumeration TSP (no ATSP yet)
#sum of all permutations
sumar = []
for path in permutations(G.nodes()):
	sum = 0
	for i in range(0, len(path)-1):
		sum+=G[path[i]][path[i+1]]['weight']
	sum+= G[path[len(path)-1]][path[0]]['weight']
	sumar.append(sum)
#print minimum
print(min(sumar))
