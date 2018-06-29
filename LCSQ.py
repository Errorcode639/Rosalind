# Given: 2 DNA strings 
# Return: the longest common subsequence
# Ex. 1: AACCTTGG 2: ACACTGTGA, return: AACTGG
import sys
sys.setrecursionlimit(1500)
dna1 = ""
dna2 = ""

with open('rosalind_lcsq.txt', 'r') as f:
	f.readline()
	for line in f:
		if '>'  in line:
			break
		else:
			dna1 += line.strip()

	for line in f:
		dna2 += line.strip()

def lcsq(s, t):
    """
    
    Given two strings s and t, find the longest common subsequence
    of s and t. Return the table that is used for each step of calculation.
    """
    m = len(s)
    n = len(t)
    C = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if s[i-1] == t[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def lcsq_len(C):
    """The length of the longest subsequence"""
    return C[-1][-1]

def lcsq_backtrack(C, s, t, i, j):
    """Given the scoring table C, strings s and t, find one of the longest common
    subsequences. Initial call of this function has i=len(s) and j=len(t)"""
    if i==0 or j==0:
        return ""
    elif s[i-1] == t[j-1]:
        return lcsq_backtrack(C, s, t, i-1, j-1) + s[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return lcsq_backtrack(C, s, t, i, j-1)
        else:
            return lcsq_backtrack(C, s, t, i-1, j)

C = lcsq(dna1, dna2)
print (lcsq_len(C))
print (lcsq_backtrack(C, dna1, dna2, len(dna1), len(dna2)))
