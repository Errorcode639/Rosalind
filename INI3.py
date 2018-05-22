# Initiate the variables: text and numbers
text = ""
a = b = c = d = 0
nums = []

# Read the input file
with open('rosalind_ini3.txt', 'r') as f:
	text = f.readline().strip()
	nums = f.readline().split()

# Covert the string to numbers
a = int(nums[0])
b = int(nums[1])+1
c = int(nums[2])
d = int(nums[3])+1

# Print the output
print(text[a:b], text[c:d])