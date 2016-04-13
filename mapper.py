f = open("recommendationVariation.txt", 'r', encoding='utf-8')
for line in f.readlines():
	line = line.strip()
	mID, sigma, rating = line.split('\t')
	print("%s,%s,%s" % (mID, sigma, rating))
