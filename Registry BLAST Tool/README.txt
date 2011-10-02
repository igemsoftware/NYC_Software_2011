README For the NYC Software 2011 BLAST Utility

This is a small part of the potential for BLAST-based tools when designing new parts. 


The python script included here will take an input DNA sequence and perform a BLASTn search on a local database. For our development purposes we use a modified version of the most current FASTA Registry dump, but this can be modified. 


Query sequence should be saved in fasta format to the Query_Sequence.fa file. This is to allow future versions of the program an easier time taking multiple query sequences.


For future development, query sequences could be cross referenced to the PICR database. This will inform you if the query is a well known CDS. 