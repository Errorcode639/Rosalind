# Given a collection of at most 10 DNA strings of equal length
# Return a consensus string and profile matrix for the collection
import numpy as np
import pandas as pd

dna = []
s = ""
with open('rosalind_cons.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>'  in line:
			dna.append(s)
			s = ""
		else:
			s += line.strip()
			

counts = []
a = c = g = t = 0
for i in range(0,len(dna[1])):
	for seq in dna:
		if seq[i] == 'A':
			a += 1
		elif seq[i] == 'C':
			c += 1
		elif seq[i] == 'G':
			g += 1
		else:
			t += 1
	counts.append([a,c,g,t])
	a = c = g = t = 0

matrix = np.matrix(counts).transpose()
df = pd.DataFrame(matrix, index=['A', 'C', 'G', 'T'])

consensus = ""
for i in range(0, len(df.columns)):
	consensus += (df.iloc[:,i].idxmax())

print(consensus)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)