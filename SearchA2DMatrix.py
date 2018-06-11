class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or target is None:
            return False
        
        i = 0; j = len(matrix[0]) - 1
        # 第一行最后一个element
        
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target: #如果当前位置等于target，返回T
                return True
            elif matrix[i][j] > target: #如果当前数字大于target，往前看一个
                j -= 1
            else: i += 1 #如果当前数字小于target，往下一行看
        return False
                
        