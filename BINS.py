# Given: 2 positive ints, sorted array A and list of ints m
# Return: Indicies of each number in m found in A, if number is not in A, return -1

# Read in the file with the lists
with open('rosalind_bins.txt', 'r') as f:
	n = int(f.readline().strip())
	k = int(f.readline().strip())
	array_A = f.readline().strip().split()
	array_M = f.readline().strip().split()

# Convert the str arrays to integers
for i in range(0, len(array_A)):
	array_A[i] = int(array_A[i])

for i in range(0, len(array_M)):
	array_M[i] = int(array_M[i])


# Perform binary search for each value in M
result = ""

def binarySearch(item, alist):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    if found:
    	return midpoint+1
    else:
    	return -1

for m in array_M:
	result += str(binarySearch(m, array_A)) + ' '

print(result)
