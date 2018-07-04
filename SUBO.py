# Given: 2 DNA strings s and t in a FASTA format
# Return: The total number of occurences of a an inexact repeat 32-40 bp long r as a substring of s
# and as a substring of t
from Bio import SeqIO

# Read in the sequences from input file
records = SeqIO.parse('rosalind_subo.txt', 'fasta')

def sub(s, t):
	"""
	Calculates the number of occurences of an inexact repeat r
	"""
	c = 0
	for j in range(32, 41):
		for i in range(len(s)-j):
			c1 = 0
			for k in range(len(t)-j):
				if hamming(s[i:i+j], t[k:k+j]) <= 3:
					c1 += 1
					if c1 > c:
						c = c1

	return c

def hamming(s1, s2):
	hammingnum = 0
	for x, y in zip(s1, s2):
		if x != y:
			hammingnum += 1
	return hammingnum

strings = []
for record in records:
	strings.append(str(record.seq))
print(str(sub(strings[0], strings[1])) + ' ' + str(sub(strings[1], strings[0])))