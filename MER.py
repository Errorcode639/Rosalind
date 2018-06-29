# Given: positive int n and sorted array A[0:n], positive int m and sorted array B[0:m]
# Return: Merged-sorted array C[0:n+m]

# Read in the file and obtain all the information
with open('rosalind_mer.txt', 'r') as f:
	n = int(f.readline().strip())
	array_A = f.readline().strip().split()
	m = int(f.readline().strip())
	array_B = f.readline().strip().split()

# Convert string arrays into ints
for i in range(0, n):
	array_A[i] = int(array_A[i])

for i in range(0, m):
	array_B[i] = int(array_B[i])

"""
MERGE ALGORITHM IN A ACADEMICALLY CORRECT FORM 

i = 0 # index of A
j = 0 # index of B

array_C = []

# Merge sorted arrays
while i < n and j < m:
	if array_A[i] < array_B[j]:
		array_C.append(array_A[i])
		i += 1
	elif array_A[i] > array_B[j]:
		array_C.append(array_B[j])
		j += 1

# Append any leftover elements of either array
if j < m:
	for k in range(j, m):
		array_C.append(array_B[k])
elif i < n:
	for k in range(i, n):
		array_C.append(array_A[k])
"""

array_C = (array_A + array_B)
array_C.sort()
result = ''
for a in array_C:
	result += str(a) + ' '

print(result)

