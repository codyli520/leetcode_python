class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or len(matrix) == 0:
            return
        
        self.sum = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.sum[i][j] = matrix[i-1][j-1] + self.sum[i][j-1] + self.sum[i-1][j] - self.sum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        return self.sum[row2][col2] - self.sum[row1-1][col2] - self.sum[row2][col1-1] + self.sum[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)