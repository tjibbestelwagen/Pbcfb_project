#! /usr/bin/env python

# partially based on examples from ' practical computing for biologists' 
# importing regular expressions module

import sys

#setting input filename
InFileName ='/home/manager/NORTH_PACIFIC/kenaispecies.txt'

#open input file for reading
InFile = open(InFileName, 'r')

#Initialize counter to keep track of line numbers
LineNumber = 0 # changing this does not affect output at this point. 

#open outputfile for writing 
#OutFileName= 'common_murre.txt'
#OutFile=open(OutFileName, 'w') # w for writing, 

WriteOutFile = True 

Species_select = raw_input("Enter species name: ") 
Year_select = int(raw_input("Enter Year: "))

OutFileName = '/home/manager/NORTH_PACIFIC/' + Species_select+ '_' + str(Year_select) +'.txt'
#OutFileName = '/home/manager/NORTH_PACIFIC/Kenai.txt'

OutFile=open(OutFileName, 'w') # w for writing, 
print OutFileName
Headerline = 'Lat\tLong\tSpecies\tYear'
#print Headerline
OutFile.write(Headerline + '\n')


#Loop through each line in the file

for Line in InFile:
    if LineNumber > 0:
        Line = Line.strip('\n')
        ElementList = Line.split('\t')
        Lat= float(ElementList[0])
        Long= float(ElementList[1])
        Species= ElementList[2]
        Year= int(ElementList[3])
        
	#replacing the space between two names (for example Common Murre) with a _
        if Species == Species_select and Year == Year_select:
            OutputString = str(Lat) + '\t' + str(Long) + '\t' + Species.replace(" ","_") + '\t' + str(Year) + '\n'
            print OutputString
            OutFile.write(OutputString)
    LineNumber += 1


InFile.close()
OutFile.close()


