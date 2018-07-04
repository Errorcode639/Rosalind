# Given: A DNA string s and a protein translated by s
# Retrun: The index od the genetic code variant used for translation

from Bio.Seq import translate

with open('rosalind_ptra.txt', 'r') as f:
	dna = f.readline().strip()
	prot = f.readline().strip()


tables = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
for i in tables:
	if prot == translate(dna, to_stop=True, table=i):
		print(i)
		break

