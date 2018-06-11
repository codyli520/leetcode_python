class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return -1
        
        start, end = 0 , len(nums)-1
        
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
        
        if nums[start]>nums[end]:
            return start
        else:
            return end