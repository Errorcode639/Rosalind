# Given: A collection of n DNA strings
# Return: The number of given strings that match their reverse complements
from Bio import SeqIO


handle = SeqIO.parse('rosalind_rvco.txt', 'fasta')

revcomp = 0
for record in handle:
	if str(record.seq) == str(record.seq.reverse_complement()):
		revcomp += 1

print(revcomp)