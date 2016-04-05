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
    # Offset user and movie id's to account for zero-index rows/cols in matrix.
    users.append(int(i)-1)
    movies.append(int(j)-1)
f.close()

# Create a sparce matrix.
import numpy as np
import scipy.sparse
from scipy.sparse import linalg
ratings = np.array(ratings).astype(np.int32)
users = np.array(users).astype(np.int32)
movies = np.array(movies).astype(np.int32)
A = scipy.sparse.csr_matrix((ratings, (users, movies)), dtype='d')

# Choose the number of dominant singular values and vectors to return.
# This is the number of characteristics to consider when making recommendations.
k = 150

# u: Unitary matrix having left singular vectors as columns.
# s: The singular values.
# vt: Unitary matrix having right singular vectors as rows.
u, s, vt = scipy.sparse.linalg.svds(A,k)

# Create diagonal matrix with sigma values.
sig = np.diag(s)

# Choose the index of a user to return recommendations for.
uid = 25

# Create et.
m,n = u.shape

data = np.array([1])
columns = np.array([uid-1]) # Offset uid to account for zero-index cols in matrix.
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
for i in top_recommendations:
  movieTitleLookup(int(i)+1) # Offset uid to account for zero-index rows in matrix.
