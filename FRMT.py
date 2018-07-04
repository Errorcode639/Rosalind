# Given: A collection of n < 10 GenBank entry IDs
# Return: The shortest of the strings associated with the IDs in FASTA format
from Bio import Entrez
from Bio import SeqIO

with open('rosalind_frmt.txt', 'r') as f:
	IDs = f.readline().strip().split()

entrez_ids = ''
for a in IDs:
	entrez_ids += a + ', '

Entrez.email = 'ada.alex.6@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=[entrez_ids], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

shortest_rec = min(records, key=lambda rec: len(rec.seq))
print shortest_rec.format("fasta")