# Given: Two GenBank IDs
# Return: The maximum global alignment score between the DNA strings associated with the IDs

from Bio import Entrez
from Bio import SeqIO

with open('rosalind_need.txt', 'r') as f:
	IDs = f.readline().strip().split()

entrez_ids = ''
for a in IDs:
	entrez_ids += a + ', '

Entrez.email = 'ada.alex.6@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=[entrez_ids], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))


# Use this program to get the FASTA sequences and then use NEEDLE from EMBOSS website to
# perform alignment
for record in records:
	print(record.format('fasta'))