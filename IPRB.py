# Given three ints k, m, n representing population containing k+m+n organisms
# k = homozygous dominant (AA)
# m = heterozygous (Aa)
# n = homozygous recessive (aa)
# Return: The probability p that two randomly selected mating organsims will profuce an individual with dominant allele

k = 18
m = 24
n = 27

total = k + m + n
p = [
	k * (k - 1),        # AA x AA
	k * m,              # AA x Aa
	m * k,              # Aa x AA
	k * n,              # AA x aa
	n * k,              # aa x AA
	m * (m - 1) * 0.75, # Aa x Aa
	m * n * 0.5,        # Aa x aa
	n * m * 0.5,        # aa x Aa
	0                   # aa x aa
	 ]

prob = sum(p) / total / (total-1)

print(prob)
