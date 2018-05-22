# Given two DNA strings s and t
# Return the Hamming distance (the number of corresponding symbols that differ in s and t)

# Initialize the Hamming distance
hamm = 0

# Read the file with both sequences
with open('rosalind_hamm.txt', 'r') as f:
	s = f.readline().strip()
	t = f.readline().strip()

for n in range(0, len(s)-1):
	if s[n] != t[n]:
		hamm += 1

print(hamm)