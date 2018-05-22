# Given positive ints n<=40 and k <= 5
# Return the total number of rabbit pairs that will be present
# after n months if we begin with 1 pair and each generation,
# every pair of reproduction-age rabbits produces a litter of k 
# rabbit pairs

n = 33
k = 2

def fib(n,k):
	if n == 2:
		return 1
	elif n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return (fib(n-1,k) + fib(n-2,k)*k)

print(fib(n,k))