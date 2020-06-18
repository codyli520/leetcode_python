class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        |123|            |789|         |741|
        |456| -reverse-> |456| -swap-> |852|
        |789|            |123|         |963|
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        find four corner coordinate and their relationship to row(i) and col(j) and matrix length(n)
        upper left 	= i,j
        upper right = j, n-i-1
        lower left	= n-j-1, i
        lower right = n-i-1, n-j-1

        Than walk through half of the matrix rows ( and column up to n-i-1), swap all four corners, then increment
        """
        n = len(matrix)
        for i in range(len(matrix)//2):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp
        