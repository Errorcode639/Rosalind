# Given: FASTQ file
# Retrun: Corresponding FASTA file

from Bio import SeqIO

for record in SeqIO.parse('rosalind_tfsq.txt', 'fastq'):
	print(record.format('fasta'))