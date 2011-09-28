import os
import urllib

def checkpart(part):
    #Check if part is available or not
    fileHandle = urllib.urlopen('http://partsregistry.org/cgi/xml/part.cgi?part='+part)
    for line in fileHandle.readlines():
        stat = ''
        if(line.startswith('<part_status>')):
            ls = line.lstrip('<part_status>')
            for char in ls:
                if(char == '<'):
                    break
                else:
                    stat += char
            #Update
            fileHandle = open('Statistics/'+str(stat)+'.txt', 'a')
            fileHandle.write(part)
            
            All_Statuses = open('Statistics/All_Statuses.txt', 'a')
            part = part.replace('\n','')
            string = part + " " + stat + "\n"
            All_Statuses.write(string)
            break
    
def main():
    PartIDs = open ('UpdatedEntryPoints.txt','r')


    count = 1
    for part in PartIDs.readlines():
        checkpart(part);
        print count
        count += 1


    
    PartIDs.close()
    All_Statuses.close()
    
main()

