class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid)==0:
            return 0
        
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    self.dfs(grid,row,column)
                    count += 1
        return count
    
    def dfs(self,grid, row, column):
        # 检查是否在matrix内，或者是不是0
        if row<0 or column<0 or row>len(grid)-1 or column>len(grid[0])-1 or grid[row][column] == "0":
            return
        # visit到的陆地就标成0
        grid[row][column] = "0"
        self.dfs(grid,row+1,column)
        self.dfs(grid,row-1,column)
        self.dfs(grid,row,column+1)
        self.dfs(grid,row,column-1)
        return
                