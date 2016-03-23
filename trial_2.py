import sys

#print("start")
matrix = []
current_id = None
ct = 0
uID = None
list = []
index = 0
for line in sys.stdin:
	if index == 0:
		line = line.strip()
		uID, mID, rate = line.split('\t')
		tup = [mID, rate]
		list.append(tup)
		current_id = uID
		#print("user " + uID + " : ")
		#print(tup)
		#print("")
		index = 1
	line = line.strip()
	uID, mID, rate = line.split('\t')
	#print('\t' + uID + '\t' + mID + '\t' + rate)	
	#print(str(ct) + '\t' + "uID : " + uID + '\t' + "mID : " + mID + '\t' + "rate : " + rate)

	
	if current_id == uID:
		#print( "same user stacking ")
		tup = [mID, rate]
		#print("user " + uID + " : ")
		#print( tup )
		#print("")
		list.append( tup )
	else:

		#print( "end of the same user ")
		if current_id:
			matrix.append([])
			matrix[ct] = [uID, list]
			ct = ct + 1
			list = []
		current_id = uID

if current_id == uID:
	tup = [mID ,rate]
	matrix.append([])
	ct = ct - 1
	list = matrix[ct]
	list.append( tup )
	matrix[ct] = list 

matrix.pop()
#print( str(len(matrix)) + " number of users " )
movieCt = 0
total = 0
for tup in matrix:
	#print("uID : " +  tup[0] )	
	#print("number of reated movies : " + str(len( tup[1])))
	print('%s\t%s' % (tup[0], str(len(tup[1]))))
	total = total + len(tup[1])
	for tup2 in tup[1]:
		movieCt = movieCt + 1
		#print(tup2)
		#(mID, rate) = tup2
		#print('\t' + mID + " " + rate )

#print( str( total ) + " nuamber of movies rated ")
#print( str( movieCt ) + " number of movies rated ")
