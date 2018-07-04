# Given: A UniProt ID of a protein
# Return: A list of biological processes in which the protein is involved
from Bio import ExPASy
from Bio import SwissProt

with open('rosalind_dbpr.txt', 'r') as f:
	uniprot = f.readline().strip()

handle = ExPASy.get_sprot_raw(uniprot)
record = SwissProt.read(handle)

go = [ref[2].split(':')[1] for ref in record.cross_references if ref[0] == 'GO' and ref[2].startswith('P')]

for entry in go:
	print(entry)