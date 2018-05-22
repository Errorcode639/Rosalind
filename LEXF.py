# Given a collection of at most 10 symbols defining an ordered
# alphabet and a positive int n <= 10
# Return all strings of length n that can be formed from the 
# alphabet, ordered lexicographically
import itertools

with open('rosalind_lexf.txt', 'r') as f:
	alpha = f.readline().strip().split(' ')
	n = int(f.readline().strip())

alpha = "".join(alpha)*n
permutations = itertools.permutations(alpha, n)


perms = sorted(list(set(permutations)))
for i in perms:
	print("".join(list(i)))	