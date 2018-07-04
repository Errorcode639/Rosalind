# Given: A DNA string s in FASTA format
# Retrun: The failure array of s


dna = ""

with open('rosalind_kmp.txt', 'r') as f:
	for line in f:
		if '>' not in line:
			dna += line.strip()

# The failure array of s is an array P of length n for which P[k] 
# is the length of the longest substring s[j:k] that is equal to some 
# prefix s[1:k-j+1], where j cannot equal 1 (otherwise, P[k] would always equal k).
# By convention, P[1]=0.

failure = [0 for i in dna]
k, cnd = 2, 0

while k < len(dna):
	if dna[k-1] == dna[cnd]:
		cnd += 1
		failure[k] = cnd
		k += 1
	elif cnd > 0:
		cnd = failure[cnd]
	else:
		failure[k] = 0
		k += 1
failure.append(0)
print(" ".join([str(i) for i in failure]))