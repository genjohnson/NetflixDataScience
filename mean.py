# Create a sparce matrix.
import numpy as np

data = np.ma.array([[1,0,2],[0,2,3],[3,4,0]])
data[data == 0] = np.ma.masked
means = np.ma.average(data, axis=1)
