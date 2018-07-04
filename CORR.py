# Given: A collection of up to 1000 reads of equal lengths in FASTA format
# Return: A list of all corrections in a form old read -> new read where each correction 
# is a single substitution
import collections

def hamming_dist(r1, r2):
	# Checks the number of differences between two sequences 
	dist = 0
	for i in range(0, len(r1)):
		if r1[i] is not r2[i]:
			dist += 1

	if dist == 1:
		return True
	else:
		return False

def reverse_comp(r1):
	# Creates a reverse complement of the sequence ex. TTAGC -> GCTAA
	reverse_d = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

	reverse = "".join([reverse_d[l] for l in r1[::-1]])
	return reverse

reads = []

# Read in the reads
with open('rosalind_corr.txt', 'r') as f:
	for line in f:
		if '>' in line:
			continue
		else:
			reads.append(line.strip())

correct_seq = []
incorrect_seq = []
# Condition 1: read was correctly sequenced in the data set and might appear at 
# least twice ( could be a reverse complement)
for read in reads:
	cnts = reads.count(read) + reads.count(reverse_comp(read))
	# Check if the read is a palidrome
	if read == reverse_comp(read):
		cnts -= 1
	if cnts > 1:
		if read not in correct_seq and reverse_comp(read) not in correct_seq:
			correct_seq.append(read)
	else:
		incorrect_seq.append(read)


# Check incorrect sequences for the Hamming distance of 1
for inc_seq in incorrect_seq:
	for cor_seq in correct_seq:
		if hamming_dist(inc_seq, cor_seq):
			print(inc_seq + '->' + cor_seq)
			break
		elif hamming_dist(inc_seq, reverse_comp(cor_seq)):
			print(inc_seq + '->' + cor_seq)
			break
	else:
		assert False




