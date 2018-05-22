# Given positive intigers n and k such that 100>=n>0
# and 10 >= k > 0
# Return the total number of partial permutations P(n,k),
# modulo 1,000,000

n = 80
k = 8

p = 1
for i in range(n-k+1, n+1):
	p = p*i

print(p%1000000)