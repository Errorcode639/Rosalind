# Given a DNA string s in FASTA format
# Return every distinct candidate protein string that can be 
# translated from ORFs of s.

n_to_aa = {'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    	   'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    	   'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    	   'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    	   'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    	   'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    	   'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    	   'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    	   'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    	   'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    	   'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    	   'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    	   'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    	   'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    	   'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    	   'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    	   }

s = ""

# Read the sequence from the FASTA file
with open('rosalind_orf.txt', 'r') as f:
	f.readline()
	for line in f:
		s += line.strip()

proteins = []

# Check for ORFs by scanning s
for n in range(0, len(s)-2):
	if s[n:n+3] == 'ATG':
		prot = ""
		has_stop = False
		for i in range(n, len(s)-2, 3):
			if n_to_aa[s[i:i+3]] is 'Stop':
				has_stop = True
				break
			else:
				prot += n_to_aa[s[i:i+3]]
		if has_stop:
			proteins.append(prot)

# Reverse complement the strand
reverse = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
s_reverse = ""

for i in range(0, len(s)):
	s_reverse += reverse[s[len(s)-i-1]]

# Check for ORFs by scanning reverse complement of s
for n in range(0, len(s_reverse)-2):
	if s_reverse[n:n+3] == 'ATG':
		prot = ""
		has_stop = False
		for i in range(n, len(s_reverse)-2, 3):
			if n_to_aa[s_reverse[i:i+3]] is 'Stop':
				has_stop = True
				break
			else:
				prot += n_to_aa[s_reverse[i:i+3]]
		if has_stop:
			proteins.append(prot)

proteins = list(set(proteins))
for p in proteins:
	print(p)