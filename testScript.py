# Return the title of a movie.
def movieTitleLookup(mid):
  with open('u.item','r',encoding='ISO-8859-1') as f:
    line = f.readlines()[mid-1]
    line = line.strip()
    movie_id,movie_title,release_date,video_release_date,imdb_url,unknown,genres = line.split('|',6)
    print(movie_title)

# Read in the data.
f = open('u.data','r',encoding='utf-8')
ratings = []
users = []
movies = []
for line in f.readlines():
    line = line.strip()
    i,j,rating,t = line.split('\t')
    ratings.append(rating)
    users.append(i)
    movies.append(j)
f.close()


# Create a sparce matrix.
import numpy as np
import scipy.sparse
from scipy.sparse import linalg
ratings = np.array(ratings).astype(np.int32)
users = np.array(users).astype(np.int32)
movies = np.array(movies).astype(np.int32)
A = scipy.sparse.csr_matrix((ratings, (users, movies)), dtype='d')

# This is not optimal since there is no advantage to having k > rank(A),
# but this is the largest value of k (number of dominant singular values
# and vectors) we can pass to svds().
k = min(A.shape)-1

# u: Unitary matrix having left singular vectors as columns.
# s: The singular values.
# vt: Unitary matrix having right singular vectors as rows.
u, s, vt = scipy.sparse.linalg.svds(A,k)

# Create diagonal matrix with sigma values.
sig = np.diag(s)

# Choose the index of a user.
uid = 25

# Create et.
m,n = u.shape

import random
# ID of the User to return recommendations for.
totalCounter = 0
counter = 0
total3 = 0
total4 = 0
total5 = 0
while True:
	i = random.randint( 1, 943 )
	#print("user id : " + str( i ))
	f = []
	

	for x in range(0, len(users)-1):
		if( users[x] == i ):
			f.append( x )	

	mf = []
	rf = []
	for x in f: 
		mf.append( movies[ x] )
		rf.append( ratings[ x ] )
	
	
	#print(f)	
	#print(mf)
	#print(rf)
	#print(tf)
	#print(tmf)
	#print(trf)
	
	data = np.array([1])
	columns = np.array([i-1])
	rows = np.array([0])

	et = scipy.sparse.csr_matrix((data, (rows, columns)), shape=(1,m), dtype='d')

	# Multiply all of the matrices.
	wt = et.dot(u)
	wt = wt.dot(sig)
	wt = wt.dot(vt)

	# Get the title of the top 10 movies.
	w = wt.flatten()
	mids_sorted = np.argsort(w)
	top_recommendations = mids_sorted[:10]
	
	movie3Rating = 0
	movie4Rating = 0
	movie5Rating = 0
	ct = 0
	for x in top_recommendations: 
		index = -1 
		for y in range(0, len(mf) -1 ):
			if( x == int(mf[ y ]) ):
				index = y
				#print("found movie " + str(x) +  " in base") 
				break	

		if index == -1  :
			#print("no movie " + str(x) + " in the data")
			continue
		else:
			ct += 1
			rating = int(rf[ index ])

			if rating >= 3 :
				movie3Rating += 1
			if rating >= 4:
				movie4Rating += 1
			if rating ==5 :
				movie5Rating += 1



	#print("Counter : " + str(ct) + " with user# " + str(i) )
	if ct > 0 :
		#print("movie3Ct: " + str(movie3Rating) + " movie4Ct: " + str(movie4Rating) + " movie5Ct: " + str(movie5Rating))
		#print("3 or above : " + str(movie3Rating / float(ct) * 100 ) )
		#print("4 or above : " + str(movie4Rating / float(ct) * 100 ) )
		#print("5	  : " + str(movie5Rating / float(ct) * 100 ) )	
		total3 += movie3Rating
		total4 += movie4Rating
		total5 += movie5Rating
		totalCounter += ct
	#print()
	
	counter += 1		
	if( counter == 1000 ):
		break
	
print("3 or above : " + str( total3 / float(totalCounter) * 100 ))
print("4 or above : " + str( total4 / float(totalCounter) * 100 ))
print("5 or above : " + str( total5 / float(totalCounter) * 100 ))
#for i in top_recommendations:
#  movieTitleLookup(i)
