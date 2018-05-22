# Given a positive int N <= 100000, a number x btwn 0 and 1, and a DNA string s
# Return the probability that if N random DNA strings having the same length as s are 
# constructed with GC-content x, then at least one of the strings equals s.
# We allow for the same random string to be created more than once.

with open('rosalind_rstr.txt', 'r') as f:
	N, gc = f.readline().strip().split()
	dna = f.readline().strip()

N, gc = int(N), float(gc)
at = 1 - gc
prob = 1    #the probability of observing string that matches with the motif
for n in dna:
	if n == 'A' or n == 'T':
		prob *= at/2
	else:
		prob *= gc/2

print(round(1 - (1-prob)**N,3))