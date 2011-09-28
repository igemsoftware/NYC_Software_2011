README for the Registry_Russ directory

These are scripts that I have used to manipulate Parts Registry data for a variety of purposes. While undergrads are free (and encouraged) to cannibalize them and use bits of code, I have not uploaded any data or representations I have made using these scripts solely because I am an iGEM Adviser this year. If you are interested, email me at rud2004@med.cornell.edu

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


Most of the scripts take arguments from the command line (i.e. python checkXMP.py <part ID>) - look at the code to see usage for each script