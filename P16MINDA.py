"""
	Minimum degree algorithm

		Cost(j) = (nzc(j)-1)(nzr(j)-1)

			nzc(j) : number of nonzero elements in column j of `active' matrix
			nzr(j) : number of nonzero elements in row j of  `active' matrix
"""

# number of nonzero elements in column j of `active' matrix
def nzc(A, cn): # A is the matrix, cn is the column number
	
	nrows = len(A)
	nzc = 0

	for i in range(nrows):
		if not A[i][cn]==0:
			nzc = nzc + 1

	return nzc

# number of nonzero elements in column j of `active' matrix
def nzr(A, rn): # A is the matrix, rn is the row number
	
	ncols = len(A[0])
	nzr = 0

	for i in range(ncols):
		if not A[rn][i]==0:
			nzr = nzr + 1

	return nzr

def cost(A, j):
	return (nzc(A, j) - 1)*(nzr(A,j) - 1)

def pivotize(A):

	nrows = len(A)
	ncols = len(A[0])

	for i in range(nrows):
		for j in range(ncols):
			print(cost(A,j))


A = [[1., 0, 0, 2., 0],
	[3., 4., 0, 5., 0],
	[6., 0, 7., 8., 9.],
	[0, 0, 10., 11., 0],
	[0, 0, 0, 0, 12.]]

pivotize(A)