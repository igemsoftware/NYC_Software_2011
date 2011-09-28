# test_curl



import os 
import sys 
import urllib
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_protein

seqlines = open('Sequences/InitialDistribution.txt', 'r')
for line in seqlines:
	part, seq = line.split(' ')
	seq = seq.replace('\n','')
	seqobj = Seq(seq, generic_dna)
	proteinobj = seqobj.translate()
	print seqobj + '\n\n'
	print proteinobj + '\n\n'
	pseq = str(proteinobj)
	print pseq + '\n\n'
	URL = 'http://pfam.sanger.ac.uk/search/sequence'
	print 'URL:\n\n' + URL + '\n\n'
	seqfileout = open('test.seq', 'w')
	seqfileout.write(pseq)
	seqfileout.close()
	lines = os.system("curl -H 'Expect:' -F seq='<test.seq' -F output=xml 'http://pfam.sanger.ac.uk/search/sequence'").read()
	count = 0
	print lines
	for x in lines:
		print 'Line ' + str(count)
		count += 1
		print x
	
	
	
