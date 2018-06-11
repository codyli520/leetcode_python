class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return -1
        
        start, end = 0, len(nums)-1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        
        return min(nums[start],nums[end])