# Given: A quality threshold, along with FASTQ entries for multiple reads
# Return: The number of reads whose average quality is below the threshold

from Bio import SeqIO

fastq = ""
below = 0
with open("rosalind_phre.txt", "rU") as handle:
	threshold = int(handle.readline())
	for record in SeqIO.parse(handle, "fastq"):
		q = record.letter_annotations['phred_quality']
		if (sum(q) / float(len(q))) < threshold:
			below += 1

print(below)


