# Given positive ints n <= 100 and m <= 20
# Return the total number of pairs of rabbits that will remain after the n-th month 
# if all rabbits live for m months

n = 87
m = 19

def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  print(ages)
  return sum(ages)

print(fib(n, m))
