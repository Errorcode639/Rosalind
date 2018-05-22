# Given a collection of k DNA strings in FASTA format
# Return a longest common substrings of the collection

sequences = []
s = ""

# Read the FASTA file and get all the sequences
with open('rosalind_lcsm.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' in line:
			sequences.append(s)
			s = ""	
		else:
			s += line.strip()

sequences.append(s)
print('got all full sequences')

# Create all the substrings from the input
def get_all_substrings(string):
   length = len(string)+1
   return [string[x:y] for x in range(length) for y in range(length) if string[x:y]]


# Create a dictionary to store the substrings in
substrings = {}
count = 1
# Generate substrings for all sequences and fill up the dictionary 
for seq in sequences:
	substr = list(set(get_all_substrings(seq)))
	print('generated ' + str(count) + ' out of ' + str(len(sequences)))
	count+=1
	if not substrings:
		for k in substr:
			substrings[k] = 1
	else:
		for k in substr:
			if k in substrings:
				substrings[k] += 1

# Find the longest substring. Check if the substring is in all given sequences
longest_substring = ""
for k,v in substrings.items():
	if v == len(sequences):
		if len(k) > len(longest_substring):
			longest_substring = k

print(longest_substring)