import sys
ct = 0
for line in sys.stdin:
	line = line.strip()
	words = line.split()
	uID = words[0]
	mID = words[1]
	rate = words[2]
	
	print('%s\t%s\t%s' % ( uID, mID, rate ))
	#ct = ct + 1
#print( ct )
