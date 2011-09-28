#!usr/bon/python

#script to extract sequence data from using biobrick IDs and store them to a csv listen

import os
import urllib

def checkpart(part):
	#Check if part is available or not
	URL = "http://partsregistry.org/fasta/parts/" + part
	filelines = urllib.urlopen(URL).readlines()
	#print filelines
	linecount = 0
	seq = str('')
	
	for line in filelines:
		#print line
		if(linecount == 0):
			print line
			linecount += 1		
		else:
			seq = seq + line
			linecount += 1
			
	SequenceFile = open('Sequences/Available.txt', 'a')
	#All_Statuses = open('Statistics/All_Ratings.txt', 'a')
	part = part.replace('\n','')
	seq = seq.replace('\n','')
	seq = seq.replace(' ','')
	print seq
	string = part + " " + seq + "\n"
	SequenceFile.write(string)
	#print string
	
    
def main():
    PartIDs = open ('Statistics/Available.txt','r') #try it out on Initial Distribution first


    count = 1
    for part in PartIDs.readlines():
        checkpart(part);
        print count
        count += 1


    
    PartIDs.close()
    All_Statuses.close()
    
main()

