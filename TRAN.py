# Given 2 DNA strings s1 and s2 of equal length
# Return the translation/transversion ratio R(s1,s2)

s1 = ""
s2 = ""

# Get both FASTA sequences
with open('rosalind_tran.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' not in line:
			s1 += line.strip()
		else:
			break

	for line in f:
		if '>' not in line:
			s2 += line.strip()
		else:
			break

translation = 0 # A to G or C to T
transversion = 0 # Other changes

for n in range(0, len(s1)-1):
	if s1[n] == 'A' and s2[n] == 'G':
		translation += 1
	elif s1[n] == 'C' and s2[n] == 'T':
		translation += 1

	elif s2[n] == 'A' and s1[n] == 'G':
		translation += 1
	elif s2[n] == 'C' and s1[n] == 'T':
		translation += 1
	else:
		if s1[n] != s2[n]:
			transversion += 1

print(round(translation/transversion, 11))