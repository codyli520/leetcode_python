class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or target is None:
            return [-1,-1]
        
        return [self.find_first(nums,target), self.find_last(nums,target)]
        
    def find_first(self, nums, target):
        if len(nums) == 0 or target is None:
            return -1
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def find_last(self, nums, target):
        if len(nums) == 0 or target is None:
            return -1
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
        