class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0,1]:
            return 1
        
        steps = [1,1]
        
        for i in range(2,n+1):
            steps.append(steps[i-2]+steps[i-1])
        
        return steps[-1]