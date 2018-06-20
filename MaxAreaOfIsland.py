class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0:
            return 0

        self.max_area = 0
        self.area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.dfs(grid,i,j,self.area)
                    self.area = 0
        return self.max_area

    def dfs(self, grid, x, y, area):
        print(area)
        if x<0 or y<0 or x>=len(grid) or y >= len(grid[x]) or grid[x][y] == 0:
            return

        grid[x][y] = 0
        self.area += 1
        self.dfs(grid,x+1,y,self.area)
        self.dfs(grid,x-1,y,self.area)
        self.dfs(grid,x,y+1,self.area)
        self.dfs(grid,x,y-1,self.area)
        self.max_area = max(self.max_area, self.area)