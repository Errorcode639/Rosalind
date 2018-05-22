
c = 1
with open('rosalind_ini5.txt', 'r') as f:
	for line in f:
		if c%2 == 0:
			print(line.strip())
		c += 1