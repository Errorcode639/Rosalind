# Given: An RNA string of at most 100 characters
# Return: The total possible number of max matchings of basepair edges in the bonding graph
from math import factorial

rna = ''
# Read in the RNA sequence
with open('rosalind_mmch.txt', 'r') as f:
	f.readline() # Don't need identifier
	for line in f:
		rna += line.strip()

min_gc, max_gc = sorted([rna.count('G'), rna.count('C')])
min_au, max_au = sorted([rna.count('A'), rna.count('U')])

gc = factorial(max_gc) // factorial(max_gc - min_gc)
au = factorial(max_au) // factorial(max_au - min_au)

print(gc * au)