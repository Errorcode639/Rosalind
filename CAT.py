# Given: An RNA string s having the same number of AU and the same number of CG
# Return: The total number of noncrossing perfect matchings of base pair edges, modulo 1,000,000


rna = ''
with open('rosalind_cat.txt', 'r') as f:
	for line in f:
		if '>' not in line:
			rna += line.strip()

def countRNAStructures(seq):
	"""
	Recursive function for counting noncrossing perfect matchings
	"""
	

# set up initial dictionary for number of matches for the sequence
cache = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0,
         'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}