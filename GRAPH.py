# Given a collection of DNA strings in FASTA format
# Return the adjacency list correcponding to O3.


sequences = {}
ID = ""
seq = ""

# Read the FASTA file and fill up the dictionary
with open('rosalind_grph.txt', 'r') as f:
	ID = f.readline().strip()[1:]
	for line in f:
		if '>' in line:
			sequences[ID] = seq
			ID = line.strip()[1:]
			seq = ""
		else:
			seq += line.strip()

sequences[ID] = seq

matching = []
# Go through all sequences and check the pre and post matching parts

for k1, v1 in sequences.items():
	for k2, v2 in sequences.items():
		if k1 != k2 and v1.endswith(v2[:3]):
			print(k1 + ' ' + k2)