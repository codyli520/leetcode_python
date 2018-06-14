class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs([], nums, 0, result)
        return result
    
    def dfs(self, subset, nums, index, result):
        result.append(subset)

        for i in range(index, len(nums)):
            self.dfs(subset+[nums[i]], nums, i+1, result)

'''
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        
        for num in nums:
            result+=[item+[num] for item in result]
        return result
        
'''