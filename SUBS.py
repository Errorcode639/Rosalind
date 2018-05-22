# Given 2 DNA strings s and t
# Return all locations of t as a substring of s

# Get the sequences
with open('rosalind_subs.txt', 'r') as f:
	s = f.readline().strip()
	t = f.readline().strip()

if t in s:
	c = t[0]
	for n in range(0, len(s)):
		if s[n] == c:
			if s[n:n+len(t)] == t:
				print(n+1)

