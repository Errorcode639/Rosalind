# Given a protein string
# Return the total number of different RNA strings from which 
# the protein could have been translated, modulo 1,000,000

freq = { 'G': 4, 'F': 2, 'L': 6, 'S': 6, 'Y': 2,
		 'STOP': 3, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
		 'Q': 2, 'R': 6, 'I':3, 'M': 1, 'T': 4,
		 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 
		 'E':2
		}

with open('rosalind_mrna.txt', 'r') as f:
	p = f.readline().strip()

total = 1

for letter in p:
	total = total * freq[letter]

print((total*freq['STOP'])%1000000)