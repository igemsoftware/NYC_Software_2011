####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

##### *** README *** #####

# TO USER: "WE" (iGEM_NYC_Software) will maintain the local database: "All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt"
# TO USER: "All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt" will be consistently updated (i.e. newer parts will be included when added to the registry)
# TO USER: User's query sequence must be saved as: "Test_Sequence.fna.txt"

##### *** NOTATIONS *** #####

#: INDICATES COMMENT
##: INDICATES COMMENT (IN ADDITION TO USING ONLY: #)
###: INDICATES A FUNCTIONAL LINE THAT IS PURPOSELY BEING COMMENT OUT, BUT WILL LATER BECOME UN-COMMENTED
####: INDICATES A FUNCTIONAL LINE THAT IS PURPOSELY BEING COMMENT OUT, AND WILL REMAIN COMMENTED (DUE TO: ALTERNATIVE METHOD ALREADY PRESENTED, SIMPLY A WORK AROUND THAT IS WORTH NOTING, ETC.)
#####: NOT USED
######: NOT USED
####### ####### ####### ####### ####### ####### #######: CODE-BLOCK SPACER

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

# Prompts for the user of this script should ideally be placed in the beginning of the run, such that the user can then let the script run without any further interuptions, therefore:

## Start prompts with:
print 'TO USER: You will be prompted %n times!'
print 'TO USER: Pressing "N" or "Enter/Return" will initiate default response'
print 'TO USER: Else press "Y" or enter desired value "%n", when applicable'
print

## Max hit displayed prompt:
X = raw_input( "How many hits would you like displayed? (default = 10)     " )
if str(X) == '':
    max_target_seqs_input = r"10"
    print 'No entry submitted. max_target_seqs = %s' % (max_target_seqs_input)
else:
    max_target_seqs_input = str(int(abs(int(X))))
    print 'Your entry: %s' % (max_target_seqs_input)
print

## GenBank download prompt:
XXX = raw_input( "Would you like to download GenBank files of top %s hits? Y/N (default = N)     " % (max_target_seqs_input) )
if str(XXX) == '':
    print 'No entry submitted. Download will not occur!'
else:
    print 'Your entry: %s' % (str(XXX))
print

raw_input('If you would like to continue this script, then press "Enter/Return"')
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

## Block of code below, will create a BLASTable database:
db_file = r"All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt" # Request this file from user
os_system_input_1 = r'makeblastdb -in ' + db_file + r' -dbtype nucl -input_type fasta'
print('Creating Database ... ... ...')
### os.system(os_system_input_1)
#### os.system('makeblastdb -in All_Parts_NO_BLANKS_SIMPLE_HEADERS.fna.txt -dbtype nucl -input_type fasta')
print('... ... ... Database Creation Completed')
print

## Block of code below, will peform BLASTn of query sequence against database
query_sequence_file = r"Test_Sequence.fna.txt" # Request this file from user
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
    print( 'Title of the hit: ' + str(description.title) )                                    # Title of the hit.
    print( 'Accession of the hit: ' + str(description.accession) )                            # Accession of the hit.
    print( 'Number of bits: ' + str(description.score) )                                      # Number of bits.  (int)
    ###########################################################################################################################################################################
    print( 'Bit score: ' + str(description.bits) )                                            # Bit score. (float)
    print( 'E value: ' + str(description.e) )                                                 # E value.  (float)
    print( 'Number of alignments for the same subject: ' + str(description.num_alignments) )  # Number of alignments for the same subject.  (int)
    print

# for blast_record in blast_records:
# for databasereport in blast_record.databasereports:

print 'DatabaseReport:' # DatabaseReport members:
print 
print( 'List of database names: ' + str(blast_record.database_name) )                                     # List of database names.  (can have multiple dbs)
print( 'Number of letters in the database: ' + str(blast_record.num_letters_in_database) )                # Number of letters in the database.  (int)
print( 'List of number of sequences in the database: ' + str(blast_record.num_sequences_in_database) )    # List of number of sequences in the database.
##############################################################################################################################################################################
print( 'List of the dates the databases were posted: ' + str(blast_record.posted_date) )                  # List of the dates the databases were posted.
print( 'A tuple of (lambda, k, h) values: ' + str(blast_record.ka_params) )                               # A tuple of (lambda, k, h) values.  (floats)
print( 'A tuple of (lambda, k, h) values: ' + str(blast_record.ka_params_gap) )                           # A tuple of (lambda, k, h) values.  (floats)
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

print 'Alignment:' # Alignment members:
print
for alignment in blast_record.alignments:
    print alignment.hit_def                                                                  # Hit definition. (str)
    blastn_report_txt_file_handle.write('> %s\n' % (alignment.hit_def))
####print alignment.hit_id                                                                   # Hit identifier. (str)
####print alignment.hsps                                                                     # A list of HSP objects.
    print
#### blastn_report_txt_file_handle.close()

print 'Finished print "Alignment" members'
print 'Still writing to file: "blastn_report.txt" ... ... ...'
print

E_VALUE_THRESH = 1.0e-0 # Request this value from user
print 'Your E_VALUE_THRESH = %s' % str(E_VALUE_THRESH)
print

# for blast_record in blast_records:
# for alignment in blast_record.alignments:
# for hsp in alignment.hsps:

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print
            print '****Alignment****'
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
print 'Finished print "Alignment" members'
print '... ... ... Finished writing to file: "blastn_report.txt"'
print

raw_input('If you would like to continue this script, then press "Enter/Return"')
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
xml_blast_handle = open(r".\blastn_report.xml")
xml_blast_text = xml_blast_handle.read()
found_BioBrick_IDs = re.findall(r"<Hit_def>(.*)</Hit_def>", xml_blast_text)
#### for Hit_def in found_BioBrick_IDs:
####     print found_BioBrick_IDs
print found_BioBrick_IDs # Below are equivalent forms to print all entries within list "found_BioBrick_IDs"
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

# Providing url links to download GenBank files of hit BioBrick IDs

print 'GenBank versions of top hitting BioBricks can be downloaded at the following urls:'
print

index = 0
while index < len(found_BioBrick_IDs):
####  print found_BioBrick_IDs[index]
    BioBrick_ID = found_BioBrick_IDs[index]
    file = BioBrick_ID + r".gb"
    print r"http://cambridgeigem.org/gbdownload/%s" % file
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

if str(XXX) == '':
    print 'No entry submitted. Download will not occur.'
elif str(XXX) == 'N':
    print 'Download will not occur due to a response: N'
elif str(XXX) == 'Y':
    print 'Downloading of GenBank files will commence due to a response: Y'
    print '... ... ... Please wait ... ... ...'
# Fetching Web Pages:
# Fetching standard Web pages over HTTP is very easy with Python:
    import urllib
    index = 0
    while index < len(found_BioBrick_IDs):
        # print found_BioBrick_IDs[index]
        BioBrick_ID = found_BioBrick_IDs[index]
        file = BioBrick_ID + r".gb"
        # print r"http://cambridgeigem.org/gbdownload/%s" % file
        urllib.urlretrieve(r"http://cambridgeigem.org/gbdownload/%s" % file, filename=file, data=r"GET")
        index += 1
else:
    print 'Invalid response! Download will not occur!'
print

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

print 'TO USER: If you would like to perform a restriction analysis on the top hit sequences, then the following websites may be useful:'
print
print r"http://www.bioinformatics.org/sms/"
print
print r"http://www.bioinformatics.org/sms/gen_fasta.html"
print r"http://www.bioinformatics.org/sms2/genbank_fasta.html"
print
print r"http://www.bioinformatics.org/sms/rest_sum.html"
print r"http://www.bioinformatics.org/sms2/rest_summary.html"
print r"http://tools.neb.com/NEBcutter2/"
print

raw_input('Press "Enter/Return" to close this window...')

####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
