
originalFile = open('result.txt', 'r')
analyzedFile = open('result2.txt', 'r')

originalMatrix = [None] * 10000
ct = 0
for line in originalFile:
	line = line.strip()
	uID, count = line.split()
	print(uID + " " + count)
	originalMatrix[ct] = [ uID, count ]
	ct = ct + 1

ct = 0
analyzedMatrix = [None] * 10000
print( )
print()
for line in analyzedFile:
	line = line.strip()
	print(line)
	uID, count = line.split()
	analyzedMatrix[ct] = [uID, count]
	ct = ct + 1

originalMatrixLength = 0
for value in originalMatrix: 
	if value != None : 
		originalMatrixLength += 1
analyzedMatrixLength = 0
for value in analyzedMatrix : 
	if value != None : 
		analyzedMatrixLength += 1
print(str(originalMatrixLength))
print(str(analyzedMatrixLength))

print('%s\t%s\t%s\t%s' % ('orgUser', 'orgMov', 'analUser', 'analMov'))
for x in range( 0, originalMatrixLength ):
	ouID = None
	ouMovie = None
	auID = None
	auMovie = None
	if x < originalMatrixLength - 1 :
		list = originalMatrix[x]
		ouID = list[0]
		ouMovie = list[1]
	if x < analyzedMatrixLength - 1:
		list= analyzedMatrix[x]
		auID = list[0]
		auMovie = list[1]
	print('%s\t%s\t%s\t%s' % ( ouID, ouMovie, auID, auMovie ))
