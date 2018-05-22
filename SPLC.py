# Given a DNA string s and a collection of substrings of s acting as introns
# Return a protein string from transcribing and translating the exons of s

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

introns = []
s = ""

with open('rosalind_splc.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' not in line:
			s += line.strip()
		else:
			print(s)
			break
	for line in f:
		if '>' not in line:
			introns.append(line.strip())


# Get rid of the introns in sequence s
for i in introns:
	char = i[0]
	#print(s)
	for n in range(0, len(s)):
		if s[n] == char:
			if s[n:n+len(i)] == i:
				s = s[:n] + s[n+len(i):]
				break

# Translate exon into protein
prot = ""
for i in range(0,len(s),3):
	#print(s[i:i+3])
	if n_to_aa[s[i:i+3]] == 'Stop':
		break
	else:
		prot += n_to_aa[s[i:i+3]]
		#print(prot)

print(prot)