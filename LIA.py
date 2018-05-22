# Given two positive ints k <= 7 and N <= 2**k. In this problem, we begin with Tom, who
# in the 0th generation has genotype AaBb. Tom has 2 children in the 1st gen,
# each of whom has 2 children and so on. Each organism always mates with an organism
# having genotype AaBb
# Return the probability that at least N AaBb organisms will belong to the k-th gen
import math

def nCi(n, i):
	f = math.factorial
	return f(n) / f(i) / f(n-i)

k, n = 7, 31

total = 2 ** k

prob = []
for i in xrange(n, total+1):
	print('n = ' + str(n) + ' i = ' + str(i))
	prob.append(nCi(total, i) * (0.25**i) * (0.75**(total-i)))

print(round(sum(prob), 3)) 