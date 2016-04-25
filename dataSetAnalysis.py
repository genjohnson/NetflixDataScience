# Written to check the dataset
# How many movies are watched for each user
import sys
def watchTest( uID):
	counter=0
	f = open('u2.base', 'r', encoding='utf-8')
	for line in f.readlines():
		line = line.strip()
		i, j, rating, t = line.split('\t')
		if int(i) == uID:
			counter+=1	
	watched = counter
	not_watched = 1682 - watched
	percentOfWatch = (watched / 1682) * 100
	print("%s,\t%s,\t%s,\t%s" % ( str(uID), str(watched), str(not_watched), str(percentOfWatch)))  	


def inList( List, Value ):
	returnList = []
	ct = 0
	for listValue in List: 
		if listValue == Value: 
			return [True, ct]
		ct = ct + 1
	return [False, -1]




def main():
	for x in range(1, 1682):
		watchTest( x )

main()
