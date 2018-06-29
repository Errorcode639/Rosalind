# Given: a positive int k, n and k arrays of size n
# Return: for each array the indecies such that A[i] = -A[i], if no such number
# exists, return -1

arrays = []

# Read in the input file
with open('rosalind_2sum.txt', 'r') as f:
	k, n = f.readline().strip().split()

	for line in f:
		array = line.strip().split()
		for i in range(0, len(array)):
			array[i] = int(array[i])
		arrays.append(array)

# Go through all arrays and check if they have a pos or neg counterelement
for array in arrays:
	found = False
	pairs = []

	# We are supposed to output the EARLIEST found PAIR
	# So, we'll collect all pairs and then figure out which was found the earliest
	for i in range(0, len(array)):
		# First element has to be positive
		if array[i] < 0:
			continue
		reverse = array[i]*(-1)
		if reverse in array:
			for j in range(i+1, len(array)):
				if array[j] == reverse:
					pairs.append([i, j])
					found = True

	# Find out which pair was found the earliest
	if found:
		earliest = 100000000
		output = []
		for pair in pairs:
			if pair[1] < earliest:
				earliest = pair[1]
				output = pair
		#print(str(array[pair[0]]) + ' ' + str(array[pair[1]]))
		print(str(pair[0]+1) + ' ' + str(pair[1]+1))

	# If nothing was found, print '-1'
	if not found:
		print('-1')

