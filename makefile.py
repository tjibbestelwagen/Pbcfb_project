#! /usr/bin/env python

# importing regular expressions module

#setting input filename
InFileName ='kenaispecies.txt'

#open input file for reading
InFile = open(InFileName, 'r')

#Initialize counter to keep track of line numbers
LineNumber = 0 # changing this does not affect output at this point. 

#open outputfile for writing 
OutFileName= 'common_murre.txt'

OutFile=open(OutFileName, 'w') # w for writing, 

WriteOutFile = True 


#Loop through each line in the file

for Line in InFile:
#	print Line
	if LineNumber > 0:
	
		Line=Line.strip('\n')
		ElementList = Line.split('\t')
		Lat	= ElementList[0]	
		Long	= ElementList[1]
		Species	= ElementList[2]
		Year	= ElementList[3]
		#print ElementList[0], ElementList [1],ElementList[2], ElementList[3]

		# need to make year into a string?
		
		if Species == 'Common Murre':
			print Line
			OutFile.write(Line) 
			OutFile.close
				

	#print LineNumber	
	LineNumber = LineNumber + 1

	

	


InFile.close() 
#outfile...
