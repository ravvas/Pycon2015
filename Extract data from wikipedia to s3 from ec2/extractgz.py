file1 = open("augindexfile",'r')

for line in file1: 

	start_qt = line.find('.gz">')
	if start_qt > 1 : 
		end_qt = line.find('<',start_qt+5)
		print line[start_qt+5 : end_qt]

