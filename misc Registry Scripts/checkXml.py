## USAGE :  python checkXml.py <part_ID>

def checkpart(part):
    #Check if part is available or not
    fileHandle = urllib.urlopen('http://partsregistry.org/cgi/xml/part.cgi?part='+part).readlines()
    for x in fileHandle:
    	print x
#     for line in fileHandle.readlines():
#         stat = ''
#         if(line.startswith('<part_status>')):
#             ls = line.lstrip('<part_status>')
#             for char in ls:
#                 if(char == '<'):
#                     break
#                 else:
#                     stat += char
#             #Update
#             fileHandle = open('Statistics/'+str(stat)+'.txt', 'a')
#             fileHandle.write(part)
#             
#             All_Statuses = open('Statistics/All_Statuses.txt', 'a')
#             part = part.replace('\n','')
#             string = part + " " + stat + "\n"
#             All_Statuses.write(string)
#             break
# 


import sys 
import urllib


for x in sys.argv[1:]:
	print "checking for part " + x
	checkpart(x)
	