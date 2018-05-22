# Given a permutation of at most 12 symbols defining an ordered
# alphabet and a positive integer n <= 4
# Return all strings of length at most n formed from alphabet,
# ordered lexicographically
import itertools

# Given variables
alphabet = "NYQAUPLEKHFT"
n = 4

# Create set of letters for permutations
letters = ""
for letter in alphabet:
	letters += (letter * n)

# Create permutations of set length 1 to n
permutations = []
for i in range(1,n+1):
	p = list(itertools.permutations(letters, i))
	for perm in p:
		permutations.append("".join(list(perm)))

# Get rid of duplicates
permutations = (list(set(permutations)))

# Sort the permutations in order of the given alphabet
permutations_sorted = sorted(permutations, key=lambda word: [alphabet.index(c) for c in word])

# Return the results
for p in permutations_sorted:
	print(p)