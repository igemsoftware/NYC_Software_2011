README for the misc Registry scripts directory

These are scripts I have developed to help with a variety of projects. They are most short bits of code that I have used in larger programs elsewhere. They are posted here because if you're reading this then you will most likely find them useful. 

You can email me at rud2004@med.cornell.edu


These will likely be the most useful for you:

checkXML.py	python checkXMP.py <part ID>	prints XML output for this part
curl.py	example curl script
EntryPointFinder.py		queries partsregistry.org/das/parts/entry_points and constructs part list
eval_ratings.py	builds ratings lists for all parts
get_sequences.py	builds sequence files in a directory
pFam.py	submits sequence from command line to pFam to generate protein domain models
PICR_query.py	queries PICR database - will find only identical nucleotide sequences
sequence-mapping.py	intermediate script to convert nucleotide to aa sequences, useful for unix pipes
updater.py	sorts through parts list to build list of only Available Parts


Most of the scripts take arguments from the command line (i.e. python checkXMP.py <part ID>) - look at the code to see usage guidelines.