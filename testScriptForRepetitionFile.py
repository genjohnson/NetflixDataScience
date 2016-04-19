# test script for the repetition file
import sys

def watchTest( uID, movies ):
	counter = 0
	returnList = [None] * len(movies)


	f = open('u.data', 'r', encoding='utf-8')
	for line in f.readlines():
		line = line.strip()
		i, j, rating, t = line.split('\t')
		if int(i) == uID:
			checkValue = inList( movies, int(j) )
			if checkValue[0]:
				returnList[ checkValue[1] ] = True
		

	print("user\t%s" % str(uID))
	ct = 0
	for value in returnList: 
		if value: 
			print("Movie\t%s\t%s" % ( movies[ct], "watched" ))
		else: 
			print("Movie\t%s\t%s" % ( movies[ct], "not watched"))
		ct = ct+1	


def inList( List, Value ):
	returnList = []
	ct = 0
	for listValue in List: 
		if listValue == Value: 
			return [True, ct]
		ct = ct + 1
	return [False, -1]





movieList = []
uID = None
counter = 0
for line in sys.stdin:
	line = line.strip() 
	if counter == 0:
		uID = int(line)
		counter = 2
		pass 
	else:
		value = int(line)
		movieList.append(value)


watchTest( uID, movieList )
