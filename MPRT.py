# Given at most 15 UniProt Database access IDs
# Return for each protein possessing the N-glycosylation motif
# output its given access ID followed by a list of locations 
# in the protein string where the motif can be found
import re, urllib2

# Get the id from the input file
proteins = []
with open('rosalind_mprt.txt', 'r') as f:
	for line in f:
		proteins.append(line.strip())


# Initiate motif regular expression string
glycisylation = '(?=(N[^P](S|T)[^P]))'  # N{P}[ST]{P}

# Download FASTA file for each protein and look for the motif regex
for p in proteins:
	id_html = 'http://www.uniprot.org/uniprot/' + p + '.fasta'
	f = urllib2.urlopen(id_html)

	seq = ''.join(f.read().split('\n')[1:-1])
	#print(seq)

	# find the motif and append it to the list
	indexes = []
	for m in re.finditer(glycisylation, seq):
		indexes.append(m.start() +1)

	# If found, print the result 
	idx = ""
	for i in indexes:
		idx += (str(i) + ' ')
	if indexes:
		print(p)
		print(idx)

