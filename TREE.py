# Given a positive int n (n <= 1000) and an adjacency list corresponding to a graph on 
# n nodes that contains no cycles
# Return the minimum number of edges that can be added to the graph to produce
# a tree

edges = []
with open('rosalind_tree.txt', 'r') as f:
	n = int(f.readline().strip())

	for line in f:
		edges.append(map(int, line.split()))

for i in edges:
	print(list(i))

print(n - len(edges) - 1)
