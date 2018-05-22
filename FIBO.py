# Given a positive integer n <= 25
# Return the value of Fibonacci(n)

def fib(n):
	# Base case
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = 20
print(fib(n))