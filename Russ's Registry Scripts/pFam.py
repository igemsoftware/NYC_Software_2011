#!usr/bin/python

#script to take sequence data and get Pfam Domains

import os 
import sys 
import urllib
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_protein

seqlines = open('Sequences/InitialDistribution.txt', 'r').readlines()
firstlines = seqlines[1:50]
for line in firstlines:
	part, seq = line.split(' ')
	seq = seq.replace('\n','')
	seqobj = Seq(seq, generic_dna)
	proteinobj = seqobj.translate()
	print seqobj + '\n\n'
	print proteinobj + '\n\n'
	pseq = str(proteinobj)
	print pseq + '\n\n'
	stop_check = pseq.rstrip('*')
	if '*' in stop_check:
		#	IF THERE ARE INTERNAL STOP CODONS, SEQUENCE PROBABLY ISNT A CDS. SHOULD ALSO TRY SPLITTING THE SEQUENCES BY STOP CODON AND QUERYING EACH 
		print "Protein sequence has internal stop codons - skipping."
	else:
		URL = "curl -H 'Expect:' -F seq=" + stop_check + " -F output=xml 'http://pfam.sanger.ac.uk/search/sequence'"
		print "URL:  " + URL + "\n\n"
		tempSeqFile = open('test.seq', 'w')
		tempSeqFile.write(stop_check)
		url = os.system(URL)
		count = 0
		print url	
	