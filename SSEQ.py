# Given 2 DNA strings s and t
# Return one collection of indicies of s in which the symbols 
# of t appear as a subsequence of s

s = ""
t = ""

with open('rosalind_sseq.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' not in line:
			s += line.strip()
		else:
			break

	for line in f:
		if '>' not in line:
			t += line.strip()
		else:
			break
i = j = 0
while i < len(s) and j < len(t):
	if s[i] == t[j]:
		print(i+1, end=" ")
		j += 1
	i += 1
print('\n')