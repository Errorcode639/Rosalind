# Given an RNA string s of length at most 80 bp having the same number of occurrences 
# of 'A' as 'U' and the same number of occurrences of 'C' as 'G'
# Return the total possible number of perfect matchings of basepair edges in the 
# bonding graph of s
import math

rna = 'AUUUUCCUCUGGACAGACGCCCAGCCGUAUGGUCGAAUAGGCUUCUUCGAGUAAGACGCACUGAAGAGCAUU'
perfects = 0

GC = rna.count('G')
UA = rna.count('A')

print(math.factorial(GC) * math.factorial(UA))