class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.dfs([],nums,0,result)
        return result
    
    def dfs(self,subset, nums, index, result):
        if subset not in result:
            result.append(subset)
            
        for i in range(index, len(nums)):
            self.dfs(subset+[nums[i]],nums,i+1,result)