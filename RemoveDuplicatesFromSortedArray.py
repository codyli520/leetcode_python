class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        prev = nums[0]
        p1 = 1
        p2 = 1
        
        while p1 < len(nums):
            
            if nums[p1] != prev:
                prev = nums[p1]
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
            p1 += 1
        
        return p2
        