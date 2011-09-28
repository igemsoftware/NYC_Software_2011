from datetime import datetime
import os
import urllib
import time as timely

def qsort1(list):
    """
    Quicksort using list comprehensions
    >>> qsort1<<docstring test numeric input>>
    <<docstring test numeric output>>
    >>> qsort1<<docstring test string input>>
    <<docstring test string output>>
    """
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def main():
    while(1):
        #Connect to the source page
        fileHandle5 = urllib.urlopen('http://partsregistry.org/das/parts/entry_points')
        junk1 = fileHandle5.readline()
        junk2 = fileHandle5.readline()
        junk3 = fileHandle5.readline()
        junk4 = fileHandle5.readline()
    
    

        wrdlist = []
        allEntries =  fileHandle5.readlines()
        for line in allEntries:
            flag = 0
            word = ''
            for letter in line:
                if(letter == '<'):
                    flag = 1
                elif(letter == '>'):
                    flag = 0
                elif(letter == ' '):
                    1
                
                elif(flag == 0):
                    word = word + letter
            if not(word.isspace()):
                wrdlist.append(word.rstrip())


        z = qsort1(wrdlist)
     
    
    
        #Get a time stamp
        time = datetime.now()

        #Save the most update log of entry points to the UpdatedEntryPoints.txt
        fileHandle2 = open ('UpdatedEntryPoints.txt', 'w')
        fileHandle2.write('Time Posted: ')
        fileHandle2.write(str(time))
        fileHandle2.write('\n')
        fileHandle2.write('Number of Entry Points: ')
        fileHandle2.write(str(len(z)))
        fileHandle2.write('\n')
        for line in z:
            fileHandle2.write(line)
            fileHandle2.write('\n')
        fileHandle2.close()

        #Spread sheet
        fileHandle3 = open ('updater-log.cvs', 'a')
        fileHandle3.write(str(len(z)))
        fileHandle3.write('\t')
        fileHandle3.write(str(time))
        fileHandle3.write('\n')
        fileHandle3.close()

        #Old Logs
        logNum = 1
        while(os.path.exists('Logs/log'+str(logNum)+'.txt')):
            logNum = logNum + 1;
        fileHandle4 = open('Logs/log'+str(logNum)+'.txt', 'w')
        fileHandle4.write('Time Posted: ')
        fileHandle4.write(str(time))
        fileHandle4.write('\n')
        fileHandle4.write('Number of Entry Points: ')
        fileHandle4.write(str(len(z)))
        fileHandle4.write('\n')
        for line in z:
            fileHandle4.write(line)
            fileHandle4.write('\n')
        fileHandle4.close()

        #Wait 24hrs
        timely.sleep(86400)

    
main()

