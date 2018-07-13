class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        
        p1 = 0 # 一直往下走
        p2 = 0 # 停留在 0
        
        while p1 < len(nums):
            if nums[p1] != 0:
                nums[p1],nums[p2] = nums[p2],nums[p1] 
                p2 += 1
            p1 += 1
        