
##### *** README *** #####

# Written by the NYC_Software 2011 iGEM Team. Direct comments / questions to rud2004@med.cornell.edu

# A Couple of notes to start out:

# USAGE is straightforward: python Registry_BLAST.py
# You will be prompted for any other parameters that may need to change. 
   
# Your query sequence must be saved as: "Query_Sequence.fa". This is to allow future versions of this program multiple queries at a time.
# This program uses Cambridge iGEM 2010's very useful genbank portal to download genbank files - if you would like.
# 


####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Prompts for the user of this script should ideally be placed in the beginning of the run, such that the user can then let the script run without any further interuptions, therefore:

## Start prompts with:
print '\n\nYou will be prompted a few times.\n'
print '"Enter/Return" will initiate default response\n'
print 
print


####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

import os
my_directory = os.getcwd()
os.chdir(my_directory)

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
# Lines below are DOS command lines for the BLAST 2.2.14 executables:
#### os.system('formatdb -i All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -p F')
#### os.system('blastall -p blastn -d All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -i Test_Sequence.fna.txt -e 10.0 -m 7 -o blastn_report.xml -T F')
# Lines below are DOS command lines for the BLAST 2.2.14 executables w/ -K = 10 & -b = 10:
#### os.system('formatdb -i All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -p F')
#### os.system('blastall -p blastn -d All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -i Test_Sequence.fna.txt -e 10.0 -T F -b 10 -K 10 -m 7 -o blastn_report.xml')
# Lines below are DOS command lines for the BLAST 2.2.17 executables:
#### os.system('formatdb -i All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -p F')
#### os.system('blastall -p blastn -d All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -i Test_Sequence.fna.txt -o blastn_report -T F')
####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Lines below are DOS command lines for the BLAST 2.2.25+ executables:


## Create a BLASTable database:
database_file = raw_input("What is the name of your database fasta file? Default is all available parts as of 10-05-10. ")
if str(database_file) == '':
    print 'No entry submitted. Default database "All_Parts_10-05-10.fa" will be used.'
    db_file = r"All_Parts_10-05-10.fa"
else:
    print "We'll use this file: " + str(database_file)
    db_file = database_file



os_system_input_1 = r'makeblastdb -in ' + db_file + r' -dbtype nucl -input_type fasta'
print('Creating Database ... ... ...')
### os.system(os_system_input_1)
#### os.system('makeblastdb -in All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -dbtype nucl -input_type fasta')
print('... ... ... Database Creation Completed')
print



####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


# Get a couple BLAST Parameters 
## Max hit displayed prompt:
X = raw_input( "How many hits would you like displayed? (default = 10)     " )
if str(X) == '':
    max_target_seqs_input = r"10"
    print 'No entry submitted. max_target_seqs = %s' % (max_target_seqs_input)
else:
    max_target_seqs_input = X 
    print 'Returning ' + max_target_seqs_input + ' alignments.'
print


####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


## Block of code below, will peform BLASTn of query sequence against database
raw_input("OK Save your query sequence to the Query_Sequence.fa File. This is done to allow multiple queries in future versions. Press Enter When Done.\n\n")
query_sequence_file = r"Query_Sequence.fa" 
# max_target_seqs_input = r"10" # Request this value from user
os_system_input_2 = r'blastn -query ' + query_sequence_file + r' -task blastn -db ' + db_file + r' -max_target_seqs ' + max_target_seqs_input + r' -out blastn_report.xml -evalue 10 -outfmt 5'
# Note: User does not have option to name the output xml file. Output file is: r"blastn_report.xml"
print('BLASTing (-version 2.2.25+) Against Local Database ... ... ...')
### os.system(os_system_input_2)
#### os.system('blastn -query Test_Sequence.fna.txt -task blastn -db All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -max_target_seqs 10 -out blastn_report.xml -evalue 10 -outfmt 5') #-html')
#### os.system('blastn -query Test_Sequence.fna.txt -task blastn -db All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -out blastn_report -evalue 10 -outfmt 0') #-html')
print('... ... ... BLASTn Completed')
print

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Lines below are to display BLAST XML Output (2.2.25+ XML)

xml_blast_handle = open(r"blastn_report.xml")

from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(xml_blast_handle)
blast_record = blast_records.next()
#### blast_record = NCBIXML.read(xml_blast_handle)#, debug=0)
#### blast_records_list = list(blast_records) # Note: This list is never used!

## The following commented lines dictates the structure into how one would "index" into the "blast_record_class"

#for blast_record in blast_records:
    # Do something with blast_record

## Commented lines that follow, are working examples that "index" into "blast_record" to display relevant information about the "BLASTn" performed

# for blast_record in blast_records:
# for header in blast_record.headers:

print 'Header:' # Headers members
print
print( 'The name of the BLAST flavor that generated this data: ' + str(blast_record.application) )         # The name of the BLAST flavor that generated this data.
print( 'Version of blast used: ' + str(blast_record.version) )                                             # Version of blast used.
print( 'Date this data was generated: ' + str(blast_record.date) )                                         # Date this data was generated.
print( 'Reference for blast: ' + str(blast_record.reference) )                                             # Reference for blast.
print( 'Name of query sequence: ' + str(blast_record.query) )                                              # Name of query sequence.
print( 'Number of letters in the query sequence: ' + str(blast_record.query_letters) )                     # Number of letters in the query sequence.  (int)
print( 'Name of the database: ' + str(blast_record.database) )                                             # Name of the database.
print( 'Number of sequences in the database: ' + str(blast_record.database_sequences) )                    # Number of sequences in the database.  (int)
print( 'Number of letters in the database: ' + str(blast_record.database_letters) )                        # Number of letters in the database.  (int)
print

# for blast_record in blast_records:
# for description in blast_record.descriptions:

print 'Description:' # Descriptions members:
print
for description in blast_record.descriptions:
	title_array = str(description.title).split(" ")
	Biobrick_ID_Hit = title_array[1]
	print( 'Hit against: ' + str(Biobrick_ID_Hit) )                              		      # Title of the hit.
	print( 'Accession of the hit: ' + str(description.accession) )                            # Accession of the hit.
	print( 'Number of bits: ' + str(description.score) )                                      # Number of bits.  (int)
	###########################################################################################################################################################################
	print( 'Bit score: ' + str(description.bits) )                                            # Bit score. (float)
	print( 'E value: ' + str(description.e) )                                                 # E value.  (float)
	print( 'Number of alignments for the same subject: ' + str(description.num_alignments) )  # Number of alignments for the same subject.  (int)
	print

# for blast_record in blast_records:
# for parameter in blast_record.parameters:

print 'Parameters:' # Parameters members:
print
print( 'Number of hits to the database: ' + str(blast_record.num_hits) )                     # Number of hits to the database.  (int)
print( 'Number of sequences: ' + str(blast_record.num_sequences) )                           # Number of sequences.  (int)
print( 'Number of sequences better than e-value: ' + str(blast_record.num_seqs_better_e) )   # Number of sequences better than e-value.  (int)
##############################################################################################################################################################################
print( 'Length of the query: ' + str(blast_record.query_length) )                            # Length of the query.  (int)
print( 'Identifier of the query sequence: ' + str(blast_record.query_id) )                   # Identifier of the query sequence. (str)
print( 'Number of letters in the database: ' + str(blast_record.database_length) )           # Number of letters in the database.  (int)
print

blastn_report_txt_file_handle = open(r"./blastn_report.txt", 'w')

# for blast_record in blast_records:
# for alignment in blast_record.alignments:

print 'Parts Hit:' # Alignment members:
print
for alignment in blast_record.alignments:
    print alignment.hit_def                                                                  # Hit definition. (str)
    blastn_report_txt_file_handle.write('> %s\n' % (alignment.hit_def))
####print alignment.hit_id                                                                   # Hit identifier. (str)
####print alignment.hsps                                                                     # A list of HSP objects.
    print
#### blastn_report_txt_file_handle.close()

print 'Finished printing "Parts Hit" '
print 'Still writing to file: "blastn_report.txt" ... ... ...'
print

E_VALUE_THRESH = 1.0e-0 # Request this value from user
print 'Your E_VALUE_THRESH = %s' % str(E_VALUE_THRESH)
print

# for blast_record in blast_records:
# for alignment in blast_record.alignments:
# for hsp in alignment.hsps:

print '************ ALIGNMENTS *************'

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print
            print 'sequence:', alignment.title                                               # Name.
            print 'length:', alignment.length                                                # Length.  (int)
            print 'e value:', hsp.expect                                                     # Expect value.  (float)
            print hsp.query[0:75] + '...'                                                    # The query sequence.
            print hsp.match[0:75] + '...'                                                    # The match sequence.
            print hsp.sbjct[0:75] + '...'                                                    # The sbjct sequence.
            #######################################################################################
            blastn_report_txt_file_handle.write('%s\n' % (''))
            blastn_report_txt_file_handle.write('%s\n' % ('****Alignment****'))
            blastn_report_txt_file_handle.write('sequence: ' + str(alignment.title) + '\n')
            blastn_report_txt_file_handle.write('length: ' + str(alignment.length) + '\n')
            blastn_report_txt_file_handle.write('e value: ' + str(hsp.expect) + '\n')
            blastn_report_txt_file_handle.write('%s\n' % (hsp.query[0:75]))
            blastn_report_txt_file_handle.write('%s\n' % (hsp.match[0:75]))
            blastn_report_txt_file_handle.write('%s\n' % (hsp.sbjct[0:75]))
            #######################################################################################
blastn_report_txt_file_handle.close()            
print
print 'Finished printing alignments...'
print '... ... ... Finished writing to file: "blastn_report.txt"'
print


####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

## test #1: NOTE: DOES NOT WORK

#blast_handle = open(r"blastn_report.xml")
#blast_records = NCBIXML.parse(blast_handle)

#for i,blast_record in enumerate(blast_records):
#    if i == 10: break
#    for alignment in blast_record.alignments:
#        for hsp in alignment.hsps:
#            #print hsp.query[0:75] + '...'
#            print alignment.hit_def

## test #2: NOTE: DOES NOT WORK

#blast_handle = open(r"blastn_report.xml")
#blast_records = NCBIXML.parse(blast_handle)
            
#for blast_record in blast_records[:10]:
#    for alignment in blast_record.alignments:
#        for hsp in alignment.hsps:
#            print alignment.hit_def

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Selective parsing of r".\blastn_report.xml":
# Specifically, extracting BioBrick IDs of hits:

import re
xml_blast_handle = open(r"blastn_report.xml")
xml_blast_text = xml_blast_handle.read()
found_BioBrick_IDs = re.findall(r"<Hit_def>(.*)</Hit_def>", xml_blast_text)
#### for Hit_def in found_BioBrick_IDs:
####     print found_BioBrick_IDs
#print found_BioBrick_IDs # Below are equivalent forms to print all entries within list "found_BioBrick_IDs"
#### print found_BioBrick_IDs[0:]
#### print found_BioBrick_IDs[0:len(found_BioBrick_IDs)]
print

# Alternatively, the list "found_BioBrick_IDs" can be generated via:

xml_blast_handle = open(r"blastn_report.xml")               # Note: This line already appears previously (therefore, redundant
from Bio.Blast import NCBIXML                               # Note: This line already appears previously (therefore, redundant)
blast_records = NCBIXML.parse(xml_blast_handle)             # Note: This line already appears previously (therefore, redundant)
blast_record = blast_records.next()                         # Note: This line already appears previously (therefore, redundant)

found_BioBrick_IDs_ = []    
for alignment in blast_record.alignments:
    found_BioBrick_IDs_.append('%s' % (alignment.hit_def))  # Create list of strings (BioBrick IDs)
    
    
####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


#Cross Reference BioBrick IDs with their information from the parts registry


Download_genbank = raw_input("Want to cross reference these hits with info from the Parts Registry? Default is yes.")

if 'n' in str(Download_genbank):
    print '"No" submitted. Skipping cross referencing.'
else:
	print 'Great! This is going to take a second though... \n\n'
	
	count = 0
	for x in found_BioBrick_IDs:
		# Fetching Web Pages:
		# Fetching standard Web pages over HTTP is very easy with Python:
		import urllib
		url_2_dl = "http://cambridgeigem.org/gbdownload/" + x + ".gb"
		#print "Retrieving " + url_2_dl
		URL = urllib.urlopen(url_2_dl).readlines()
		header = URL[0:2]
		header_for_printing = "".join(header)
		if count == 0:
			print "These parts are aligning to your query: \n\n"
		count = count + 1
		print header_for_printing
print


####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Providing url links to download GenBank files of hit BioBrick IDs
raw_input('Moving on to display locations to GenBank files for these hits. Please press "Enter"')
print


print 'GenBank versions of top hitting BioBricks can be downloaded at the following urls:'
print

index = 0
while index < len(found_BioBrick_IDs):
####  print found_BioBrick_IDs[index]
    BioBrick_ID = found_BioBrick_IDs[index]
    file = BioBrick_ID + r".gb"
    print str(index) + r") http://cambridgeigem.org/gbdownload/%s" % file
    index += 1
print

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


# Ask if user would like to download GenBank files:
# The three websites of interest are:

# r"http://2010.igem.org/Team:Cambridge/Tool/GenBank"
# r"http://cambridgeigem.org/asGenBank.php?part=BBa_%s % input (ex: input = r"S04179")
# r"http://cambridgeigem.org/gbdownload/%s" % file (ex: file = r"BBa_S04179.gb")

#  Note: XXX is defined because XXX was determined by the code below (which was presented at the beginning of the script)
#  XXX = raw_input( "Would you like to download these files right now? Y/N (default = N)     " )
####  print str(XXX)

Download_genbank = raw_input("Do you want to view the full GenBank files for any of these? Enter the number - otherwise just press enter. ")

if str(Download_genbank) == '':
    print 'No entry submitted. Download will not occur.'
else:
	print 'Downloading file for ' + found_BioBrick_IDs[int(Download_genbank)]
	print '... ... ... Please wait ... ... ...\n\n'
	# Fetching Web Pages:
	# Fetching standard Web pages over HTTP is very easy with Python:
	import urllib
	BioBrick_ID = found_BioBrick_IDs[int(Download_genbank)]
	file = BioBrick_ID + r".gb"
	url_2_dl = "http://cambridgeigem.org/gbdownload/" + BioBrick_ID + ".gb"
	print "Retrieving file using Cambridge iGEM 2010's portal: " + url_2_dl + "\n\n"
	URL = urllib.urlopen(url_2_dl).readlines()
	URLforprinting = "".join(URL)
	print URLforprinting
print



####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
print "\nDone\n"
####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
