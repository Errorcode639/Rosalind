# Given: A positive int n and an array A of ints
# Return: The number of swaps performed by the insertion algorithm


# Read in the data
n = 0
with open('rosalind_ins.txt', 'r') as f:
	n = int(f.readline().strip())
	array = f.readline().strip().split()

for i in range(0, len(array)):
	array[i] = int(array[i])

# Perform insertion sort
num_swaps = 0
for i in range(1, len(array)):
	k = i
	while k > 0 and array[k] < array[k-1]:
		temp = array[k]
		array[k] = array[k-1]
		array[k-1] = temp
		num_swaps += 1
		k -= 1

print(num_swaps)