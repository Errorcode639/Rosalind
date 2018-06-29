# Given: A simple graph vertices in the edge list format
# Return: An array where each entry is the degree of the vertex

# Read in the edges 
edges = []
with open('rosalind_deg.txt', 'r') as f:
	f.readline()
	for line in f:
		e = line.split()
		edge = []
		for n in e:
			edge.append(int(n))
		edges.append(edge)

#print(edges)

# Figure out the max value
max_v = max(max(edge) for edge in edges)
#print(max_v)

# Loop through each vertex and count it's degree
result = ''
for vertex in range(1, max_v+1):
	degree = 0
	for edge in edges:
		if vertex in edge:
			degree += 1
	result += str(degree) + ' '

print(result)
