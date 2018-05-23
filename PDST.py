# Given a collection of n <= 10 DNA strings of equal length
# Return the matrix D corresponding to the p-distance on the given strings


sequences = []
seq = ""

with open('rosalind_pdst.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' in line and seq:
			sequences.append(seq)
			seq = ""
		else:
			seq += line.strip()

sequences.append(seq)

row = ""
for seq1 in sequences:
	for seq2 in sequences:
		differences = 0.0
		length = len(seq1)
		for i in range(0,length):
			if seq1[i] != seq2[i]:
				differences += 1
		row = row + str(round(differences/length, 5)) + " "
	print(row)
	row = ""