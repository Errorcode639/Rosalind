# Given a positive integer n < 6
# Return the total number of signed permutations of length n, 
# followed by a list of all such permutations

from itertools import permutations, product

n = 3
numbers = list(permutations(range(1, n + 1)))
signs = list(product('-+', repeat=n))

results = list(product(numbers, signs))
print(len(results))
for l in results:
	for i in range(0,len(l[0])):
		if l[1][i] == '-':
			print(l[1][i]+str(l[0][i]), end=" ")
		else:
			print(str(l[0][i]), end=" ")
	print('\n', end=" ")