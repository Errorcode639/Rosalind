# Given a DNA sting s and an array A containing at most 20 numbers between 0 and 1
# Return an array B having the same length as A in which B[k] represents
# the common logarithm of the probablility that a random string constructed
# with the GC-concent found in A[k] will match s exactly

from math import log10

A = []

# Read the input file
with open('rosalind_prob.txt', 'r') as f:
	dna = f.readline().strip()
	nums = f.readline().strip().split()

# Convert strings to floats 
for n in nums:
	A.append(float(n))


B = []
# Go through the gc percentages in A
for percentage in A:

	# Initiate chance, %gc, %at
	chance = 1.0
	gc = percentage * 0.5
	at = (1-percentage) * 0.5

	# For each character in the dna string, mulitplt chance given certain character
	for c in dna:
		if c == 'A' or c == 'T':
			chance *= at
		else:
			chance *= gc

	B.append(round(log10(chance), 3))

for n in B:
	print(n, end=" ")
print('\n', end=" ")