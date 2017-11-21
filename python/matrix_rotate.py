import unittest

def rotate_ccw(matrix):
	n = len(matrix) # assumes square
	for i in range(0, int(n/2)):
		corner = matrix[i][i]

		## Top row goes left
		for j in range(i+1,n-i):
			matrix[i][j-1] = matrix[i][j]

		## Right column goes up
		for j in range(i+1,n-i):
			matrix[j-1][n-i-1] = matrix[j][n-i-1]
		
		## Bottom row goes right
		for j in range(i+1,n-i):
			# matrix[n-i-1][(n-i-1)-(j-i-1)] = matrix[n-i-1][(n-i-1)-(j-i-1)-1]
			matrix[n-i-1][n-j] = matrix[n-i-1][n-j-1]
		
		## Left column goes down
		for j in range(i+1,n-i):
			# matrix[(n-i-1)-(j-i-1)][i] = matrix[(n-i-1)-(j-i-1)-1][i]
			matrix[n-j][i] = matrix[n-j-1][i]

		matrix[i+1][i] = corner
	
	return None


class TestRotateCCW(unittest.TestCase):
	def test_2x2(self):
		in_matrix = [
			[1, 2],
			[4, 3]]
		res_matrix = [
			[2, 3],
			[1, 4]]

		rotate_ccw(in_matrix)

		self.assertEqual(in_matrix, res_matrix)

	def test_3x3(self):
		in_matrix = [
			[1, 2, 3],
			[8, 0, 4],
			[7, 6, 5]]
		res_matrix = [
			[2, 3, 4],
			[1, 0, 5],
			[8, 7, 6]]

		rotate_ccw(in_matrix)
		self.assertEqual(in_matrix, res_matrix)

	def test_4x4(self):
		in_matrix = [
			[11, 12, 13, 14],
			[22, 23, 24, 15],
			[21, 26, 25, 16],
			[20, 19, 18, 17]]
		res_matrix = [
			[12, 13, 14, 15],
			[11, 24, 25, 16],
			[22, 23, 26, 17],
			[21, 20, 19, 18]]

		rotate_ccw(in_matrix)
		self.assertEqual(in_matrix, res_matrix)

	def test_5x5(self):
		in_matrix = [
			[11, 12, 13, 14, 15],
			[26, 27, 28, 29, 16],
			[25, 34, 35, 30, 17],
			[24, 33, 32, 31, 18],
			[23, 22, 21, 20, 19]]
		res_matrix = [
			[12, 13, 14, 15, 16],
			[11, 28, 29, 30, 17],
			[26, 27, 35, 31, 18],
			[25, 34, 33, 32, 19],
			[24, 23, 22, 21, 20]]

		rotate_ccw(in_matrix)
		self.assertEqual(in_matrix, res_matrix)

	def test_1x1(self):
		in_matrix = [[1]]
		res_matrix = [[1]]

		rotate_ccw(in_matrix)
		self.assertEqual(in_matrix, res_matrix)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestRotateCCW)
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)