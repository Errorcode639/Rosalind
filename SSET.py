# Given a positive int n <= 1000
# Return the total number of subsets of { 1, 2, ..., n} modulo 1,000,000
# AKA Power set which can be easily calculated through 2**n

n = 987

combinations = 2**n
print(str(combinations % 1000000))