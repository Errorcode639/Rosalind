# Given: A simple graph with n vertices in the edge list format
# Return: An array D where each element is the sum of the degrees of i's neighbours

adj_dict = {}

# Read in the input file and create a dictionary for edges
with open('rosalind_ddeg.txt', 'r') as f:
	n, e = f.readline().strip().split()
	for line in f:
		v1, v2 = line.strip().split()
		if v1 not in adj_dict:
			#print(v1 + ' not in dict. Adding...')
			adj_dict[v1] = [v2]
		else:
			adj_dict[v1].append(v2)

		if v2 not in adj_dict:
			#print(v2 + ' not in dict. Adding...')
			adj_dict[v2] = [v1]
		else:
			adj_dict[v2].append(v1)

# Fill in any vertices that don't have any edges
for i in range(1, int(n)+1):
	if str(i) not in adj_dict:
		adj_dict[str(i)] = []

result = ''
for i in range(1, int(n)+1):
	degree = 0
	list_of_neighbours = adj_dict[str(i)]
	for vert in list_of_neighbours:
		degree += len(adj_dict[vert])
	result += str(degree) + ' '

print(result)