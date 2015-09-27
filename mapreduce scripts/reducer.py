#!/usr/bin/env python
import sys
KeywordTotal = 0
oldKey = None

 
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
 
    thisKey, thisnum = data
    if oldKey and oldKey != thisKey:
	print oldKey, " ", KeywordTotal
        oldKey = thisKey
        KeywordTotal = 0
 
    oldKey = thisKey
    KeywordTotal += int(thisnum)
    
if oldKey != None:
    print oldKey, " ", KeywordTotal
