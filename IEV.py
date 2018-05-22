# Given six nonnegative ints that correspond to the number of 
# couples in the population possessing each genotype pairing
# for a given factor
# return the expected number of offspring displaying dominant 
# phenotype, under the assumption that every couple has exactly 
# 2 offspring.

with open('rosalind_iev.txt', 'r') as f:
	ints = f.readline().strip().split()

p = [
	 int(ints[0])*2*1,		# AA-AA, P=1
	 int(ints[1])*2*1,		# AA-Aa, P=1
	 int(ints[2])*2*1,		# AA-aa, P=1
	 int(ints[3])*2*0.75,	# Aa-Aa, P=0.75
	 int(ints[4])*2*0.5,	# Aa-aa, P=0.5
	 int(ints[5])*2*0		# aa-aa, P=0
	 ]

print(sum(p))