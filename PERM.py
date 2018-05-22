# Given a positive int n <= 7
# Return the total number of permutations of length n followed
# by a list of all such permutations
import itertools

n = 5
per_num = 1

# Compute the number of permutations
for n in range(1,n+1):
	per_num = per_num * n 

print(str(per_num))

s = ""
for n in range(1, n+1):
	s += str(n)

# Compute the permutations of n
perms = itertools.permutations(s,n)
for n in perms:
	for i in n:
		print(i, end=" ")
	print('\n', end=" ")