# Given: a positive in n and an array A[0:n]
# Return: a sorted array A

with open('rosalind_ms.txt', 'r') as f:
	n = int(f.readline().strip())
	array = f.readline().strip().split()

for i in range(0, n):
	array[i] = int(array[i])

array.sort()
result = ''
for n in array:
	result += str(n) + ' '

print(result)