"""
Gaussian Elimination with Scaled Partial Pivoting

Written By:
    Nick Oka
    Henzi Kou

MATH 352
Final Project
"""
import random

def scaledGaussianElimination(A, b, matrix):
	# Performs Gaussian elimination on a given matrix A and b
	# Also calculates the scale and ratio vectors to determine the pivot row
	length = len(A)

	I = [i for i in range(1,length + 1)]			# Index vector
	S = maxVectors(A)								# Scaled vector

	print()
	print("A =")
	print(A)
	print("\nb =")
	print(b)
	print()
	# Print matrix Ax = b
	print("\nMatrix of Ax = b:")

	for x in matrix:
		print(x)
	print()
	print("S = ", S, "\n")

	# List of pivot rows
	visited = []

	# Iterate through each a(i,j) value in the matrix A
	for i in range(length):
		count = 0
		ratioVector = []							# Ratio vector

		for x in matrix:
			# If pivot row is already visited then set the ratio as 0 in the
			# ratio vector.
			if count in visited:
				ratioVector.append(0)

			# Else take the ratio of the elements in the current column and
			# append to the ratio vector.
			else:
				value = abs(x[i]) / S[count]		# Obtain the ratio
				ratioVector.append(value)			# Add value to ratioVector

			# Move pointer to next element in the column
			count += 1

		print("Iteration:", i + 1)
		print("Current ratio vector:", ratioVector)
		
		# Find the largest ratio and assign the respective row as the pivot row
		maxPosition = ratioVector.index(max(ratioVector))
		print("Pivot Position:", maxPosition + 1)

		# Add index of pivot row to rows in matrix already visited
		visited.append(maxPosition)
		maxIndex = I.index(maxPosition + 1)

		# Swap the order of the pivot rows in the index vector
		temp_maxPosition = I[maxIndex]
		temp_current = I[i]
		I[maxIndex] = temp_current
		I[i] = temp_maxPosition

		# Print the reindexed index vector
		print("I:", I, "\n")

		for j in range(0, length):
			temp_list = []

			for k in range (length + 1):
				# Apply row reduction on subsequent rows besides the pivot row
				if j not in visited and j != maxPosition:
					x = matrix[j][k] - matrix[maxPosition][k] * matrix[j][i] / matrix[maxPosition][i]
				else:
					x = matrix[j][k]
				temp_list.append(x)

			matrix[j] = temp_list
		
		# Print the intermediate matrix
		print("Intermediate Matrix:")

		for x in matrix:
			print(x)

		print()

	# sort the matrix based on index
	track_list = [0]*length
	counter = 0
	for x in matrix:
		track_list[counter] = matrix[I[counter] - 1]
		counter = counter + 1

	print("After using back substitution:")

	length = len(track_list)

	# perform back substitution	
	go = [0] * length
	for i in range(length-1, -1, -1):
		s = 0
		for j in range(i, length):
			s += (track_list[i][j] * go[j])
		go[i] = (track_list[i][length] - s) / track_list[i][i]

	return go

def maxVectors(A):

	S = [] # list of the maximum scaled vectors
	for x in A:
		test_list = []
		for i in x:
			test_list.append(abs(i))
		value = max(test_list)
		S.append(value)
	return S

def driver():
	# Main driver function
	print("Solve a system of linear equations using Gaussian elimination with scaled vectors.")

	while (True):
		print("\nSelect from the following options:")
		print("\t0 - Random 5x5 Matrix")
		print("\t1 - 5x5 Hilbert Matrix")
		print("\t2 - Random 12x12 Matrix")
		print("\t3 - Random 20x20 Matrix")
		print("\t4 - Random matrix of size n")
		print("\t5 - Enter your own matrix\n")

		answer = input("Enter value: ")

		valid = ["0", "1", "2", "3", "4", "5", "6"]

		A = []
		b = []
		n = 0

		if (answer not in valid):
			# If answer is not one of the valid answers then raise an error exception
			print("Not valid input.")

			pass

		elif (answer == valid[0]):
			# Random 5x5 matrix
			n = 5

			# Create matrix A
			for i in range(n):
				rows = []
				for j in range(n):
					rows.append(random.uniform(-100, 100))

				A.append(rows)

			# Create vector b
			for k in range(n):
				b.append(random.uniform(-100, 100))

			break

		elif (answer == valid[1]):
			# 5x5 Hilbert matrix
			A = [[1,1/2,1/3,1/4,1/5],[1/2,1/3,1/4,1/5,1/6],[1/3,1/4,1/5,1/6,1/7],[1/4,1/5,1/6,1/7,1/8],[1/5,1/6,1/7,1/8,1/9]]
			b = [1,1,1,1,1]
			n = 5
			
			break
		
		elif (answer == valid[2]):
			# Random 12x12 matrix
			n = 12

			# Create matrix A
			for i in range(n):
				rows = []
				for j in range(n):
					rows.append(random.uniform(-100, 100))

				A.append(rows)

			# Create vector b
			for k in range(n):
				b.append(random.uniform(-100, 100))
			
			break

		elif (answer == valid[3]):
			# Random 20x20 matrix
			n = 20

			# Create matrix A
			for i in range(n):
				rows = []
				for j in range(n):
					rows.append(random.uniform(-100, 100))

				A.append(rows)

			# Create vector b
			for k in range(n):
				b.append(random.uniform(-100, 100))
			
			break

		elif (answer == valid[4]):
			# Random matrix of size n
			size = input("Enter a positive integer for n: ")
			n = int(size)

			# Create matrix A
			for i in range(n):
				rows = []
				for j in range(n):
					rows.append(random.uniform(-100, 100))

				A.append(rows)

			# Create vector b
			for k in range(n):
				b.append(random.uniform(-100, 100))

			break

		elif (answer == valid[5]):
			# Inputted matrix
			# Determine the size of a nxn matrix
			size = input("Enter a positive integer for n: ")
			n = int(size)

			print("Enter values for the rows of matrix A from left to right.")

			# Create matrix A
			for i in range(n):
				rows = [None] * n
				for j in range(n):
					val = input("Enter a number for matrix A in row {}: ".format(i + 1))
					rows[j] = int(val)
					print(rows)
					
				A.append(rows)

			print("\nMatrix A:")

			for x in A:
				print(x)

			print("Enter values for the vector b.")

			# Create vector b
			for k in range(n):
				val = input("Enter a number for vector b: ")
				b.append(int(val))

			break
		elif (answer == valid[6]):
			# testing matrices A and b from in-class example
			A = [[-1,1,0,-3],[1,0,3,1],[0,1,-1,-1],[3,0,1,2]]
			b = [4,0,3,1]

			break

	matrix = []

	# Combine matrix A and vector b into a single matrix
	for i in range(len(A)):
		tmp = list(A[i])
		tmp.append(b[i])
		matrix.append(tmp)

	# Perform Gaussian elimination on matrices
	x = scaledGaussianElimination(A, b, matrix)

	final = []

	# Append result into a final matrix to print
	for i in x:
		final.append(i)

	print("X =", final)

# this code should work with either python or python3
if __name__ == "__main__":
	driver()
