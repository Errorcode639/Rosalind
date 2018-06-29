# Given a positive int k, positive int n and k arrays of size n containing positive ints
# Return: For each array, output an element of this array occuring more than n/2 times

result = ''

with open('rosalind_maj.txt', 'r') as f:
	# Get the numbers and the frequency
	k, n = f.readline().strip().split()
	n = int(n)
	freq = n/2
	# Iterate through each array and look for an element with desired frequency
	for i in range (0, int(k)):
		found = False
		array = f.readline().strip().split()
		# Calculate the frequency of each element
		for a in array:
			element_freq = array.count(a)
			# If found, append to the result string
			if element_freq > freq:
				result += a + ' '
				found = True
				break
		# If we didn't find the element, append '-1'
		if not found:
			result += '-1 '

print(result)