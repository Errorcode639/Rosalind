# K-mer Composition
# Given a DNA string s in FASTA format
# Return: A 4-mer composition of s
from itertools import product

dna = ""

# Open the FASTA file and read in the DNA string
with open('rosalind_kmer.txt', 'r') as f:
	f.readline()
	for line in f:
		dna += line.strip()

# Create all possible k-mers specified by the problem
k_mers = (''.join(k) for k in product('ACGT', repeat=4))

# Count the number of appearances of each k-mer and store in in organized list
# Counting in overlapping k-mers
# ex. 'AAAAA' = 2 'AAAA' k-mers 
k_mers_appearances = []

for k in k_mers:
	k_mers_appearances.append(sum(dna[i:].startswith(k) for i in range(len(dna))))

# Create a result output
result = ""
for n in k_mers_appearances:
	result += str(n) + ' '

print(result)