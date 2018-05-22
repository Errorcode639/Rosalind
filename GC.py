# Given at most 10 DNA strings in FASTA format
# Return the ID of the string with the highest GC-concent

# Initialize the variables
id = ""
gc = 0
max_gc = 0
max_id = ""
l_len = 0

# Open FASTA file
with open('rosalind_gc.txt', 'r') as f:
	for line in f:
		if '>' in line:
			if l_len != 0:
				gc = gc/l_len * 100
			if gc > max_gc:
				max_gc = gc
				max_id = id
			# Get the id of current sequence
			id  = line.strip()
			gc = 0
			l_len = 0
		if '>' not in line:
			l_len += len(line.strip())
			# Calculate the GC content of current sequence
			for n in line:
				if n == 'C' or n == 'G':
					gc += 1

# Check the last sequence
gc = gc/l_len * 100
if gc > max_gc:
	max_gc = gc
	max_id = id

# Print the result
print(max_id[1:] + '\n' + str(max_gc) + '%')