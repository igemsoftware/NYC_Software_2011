


from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

sequencefile = open('Sequences/InitialDistribution.txt', 'r').readlines()


def getPfams(aa):
	
	
	

for line in sequencefile:
	print line
	line = line.replace('\n', '')
	part, sequence = line.split(' ')
	seq = Seq(sequence, generic_dna)
	print seq
	aa = seq.translate(table="Bacterial")
	print seq
	print aa
	
	getPfams(aa)


