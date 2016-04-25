import numpy as np
import scipy.sparse
from scipy.sparse import linalg

def movieTitleLookup(mid):
  """
  Print the title of a movie.

  Arguments:
  mid -- the ID of a movie
  """
  with open('u.item', 'r', encoding='ISO-8859-1') as f:
    line = f.readlines()[mid - 1]
    line = line.strip()
    movie_id, movie_title, release_date, video_release_date, imdb_url, unknown,genres = line.split('|', 6)
    print(movie_title)

def svd(k=26):
  """
  Return the singular value decomposition of a matrix of adjusted ratings.

  Arguments:
  k -- the number of singular values to return (default 150)
  """
  # Read in the data.
  f = open('u.data', 'r', encoding='utf-8')
  ratings = []
  users = []
  movies = []
  for line in f.readlines():
    line = line.strip()
    i,j,rating,t = line.split('\t')
    ratings.append(rating)
    # Offset user and movie id's to account for zero-index rows/cols in matrix.
    users.append(int(i) - 1)
    movies.append(int(j) - 1)
  f.close()

  # Create a sparce matrix.
  ratings = np.array(ratings).astype(np.int32)
  users = np.array(users).astype(np.int32)
  movies = np.array(movies).astype(np.int32)
  A = scipy.sparse.csr_matrix((ratings, (users, movies)), dtype='d')

  # Calculate global average rating
  global_average_rating = ratings.mean()
  N = 25

  # Caculate the average rating provided by each user and the average rating
  # of each movie.
  M,N = A.shape

  row_sums = A.sum(axis=1)
  row_nnzs = A.getnnz(axis=1)
  average_rating_by_user = []
  for rid in range(M):
    average_rating_by_user.append(float(row_sums[rid] / row_nnzs[rid]))

  average_rating_by_movie = []
  better_average_rating_by_movie = []
  col_sums = A.sum(axis=0)
  col_nnzs = A.getnnz(axis=0)
  for cid in range(N):
    average_rating_by_movie.append(float(col_sums[0,cid] / col_nnzs[cid]))
    # test = (global_average_rating*N + col_sums[0,cid])
    # test2 = (N + col_nnzs[cid])
    better_average_rating_by_movie.append(((global_average_rating*N + col_sums[0,cid]) / (N + col_nnzs[cid])))

  # Adjust non-zero ratings to account for average per user and per movie.
  adjusted_ratings = []
  elements = A.nonzero()
  for i in range(len(elements[0])):
    rating_user_index = elements[0][i]
    rating_movie_index = elements[1][i]
    adjusted_rating = ratings[i] - average_rating_by_user[rating_user_index] - better_average_rating_by_movie[rating_movie_index] #average_rating_by_movie[rating_movie_index]
    adjusted_ratings.append(adjusted_rating)

  # Create a sparce matrix of the adjusted ratings.
  B = scipy.sparse.csr_matrix((adjusted_ratings, (users, movies)), dtype='d')

  return scipy.sparse.linalg.svds(B, k)

def recommendMoviesForUser(uid, num_movies):
  """
  Return recommended movies for a given user.

  Arguments:
  uid -- the ID of a user to return recommendations for
  num_movies -- the number of movies to recommend
  """
  u, s, vt = svd()
  # Create diagonal matrix with sigma values.
  sig = np.diag(s)

  # Create et.
  m,n = u.shape

  data = np.array([1])
  columns = np.array([uid - 1])  # Offset uid to account for zero-index cols in matrix.
  rows = np.array([0])

  et = scipy.sparse.csr_matrix((data, (rows, columns)), shape=(1, m), dtype='d')
  # Multiply all of the matrices.
  wt = et.dot(u)
  wt = wt.dot(sig)
  wt = wt.dot(vt)

  # Get the title of the top num_movies movies.
  w = wt.flatten()
  mids_sorted = np.argsort(w)
  top_recommendations = mids_sorted[:num_movies]
  for i in top_recommendations:
    movieTitleLookup(int(i) + 1)  # Offset uid to account for zero-index rows in matrix.

recommendMoviesForUser(uid=5, num_movies=10)
