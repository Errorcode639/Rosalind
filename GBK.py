# Given: A genus name, and two dates
# Return: Number of Nucleotide GenBank entries for the given genus that were published
# between the two provided dates

from Bio import Entrez

with open('rosalind_gbk.txt', 'r') as f:
	genus = f.readline().strip()
	date1 = f.readline().strip()
	date2 = f.readline().strip()

querry = '"%s"[Organism] AND ("%s"[PDAT] : "%s"[PDAT])' %(genus, date1, date2)
handle = Entrez.esearch(db='nucleotide', term=querry)
record = Entrez.read(handle)
print(record['Count'])