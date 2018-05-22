# Given at most 50 DNA strings of approx. equal length in FASTA format
# Return a shortest superstring containing all the given strings (thus corresponding
# to a reconstructed chromosome)

fragments = []
seq = ""

with open('rosalind_long.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>' in line:
			fragments.append(seq)
			seq = ""
		else:
			seq += line.strip()

fragments.append(seq)

# Use recursive function to asseble the superstring
def find_overlaps(reads, genome=''):
	if len(reads) == 0:  # Base case
		return genome

	elif len(genome) == 0:  # Starting case where we don't have anything assbled yet
		genome = reads.pop(0)
		return find_overlaps(reads, genome)

	else:
		# Asseble the rest of the reads
		for i in range(len(reads)):
			a = reads[i]
			l = len(a)

			# At least half the size of the reads
			for p in range(l/2):
				q = l - p

				# Try to fit the sequence in front
				if genome.startswith(a[p:]):
					reads.pop(i)
					return find_overlaps(reads, a[:p] + genome)

				# Try to fit the sequence in back
				if genome.endswith(a[:q]):
					reads.pop(i)
					return find_overlaps(reads, genome + a[q:])

print(find_overlaps(fragments))