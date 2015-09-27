#!/usr/bin/env python
import sys
for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) == 4 : 
            project,keyword,frequency,size = data
            if int(frequency) > 100 and project == "en":
		print "{0}\t{1}".format(keyword,frequency)
