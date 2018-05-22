# Given a DNA string in FASTA format
# Return the position and length of every reverse palindrome
# in the string having length btwn 4 and 12

reverse = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
s = ""
with open('rosalind_revp.txt', 'r') as f:
	f.readline()
	for line in f:
		s += line.strip()

		
for j in range(2,7):
	for n in range(0,len(s)-j):
		p1 = s[n:n+j]
		p2 = s[n+j:n+j*2]
		p2_rev = ""
		for i in range(0,len(p2)):
			p2_rev += reverse[p2[i]]
		if p1 == p2_rev[::-1]:
			print(str(n+1) +  ' ' + str(j*2))
