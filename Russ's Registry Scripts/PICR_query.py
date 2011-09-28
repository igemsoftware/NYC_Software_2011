#!sur/bin/python

#script to parse sequences, convert to AA, BLAST query to PICR with getUPIforBLAST

#PICR query with URL will only access ENSEMBL and SWISSPROT

import os
import sys 
import urllib
import urllib2
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_protein


director = urllib2.OpenerDirector()


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
	stop_check = pseq.rstrip('*')
	if '*' in stop_check:
		#	IF THERE ARE INTERNAL STOP CODONS, SEQUENCE PROBABLY ISNT A CDS. SHOULD ALSO TRY SPLITTING THE SEQUENCES BY STOP CODON AND QUERYING EACH 
		print "Protein sequence has internal stop codons - skipping."
	else:
		URL = "http://www.ebi.ac.uk/Tools/picr/rest/getUPIForSequence?sequence=" + pseq + "&database=ENSEMBL"	
		
		print 'URL:\n\n' + URL + '\n\n'

		request = urllib2.Request(URL)

		response = director.open(request)
	
		print response.info()
		
		print response
		
		