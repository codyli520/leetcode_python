class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        first, last = -1, -1
        
        if not nums:
            return [first,last]
        
        start, end = 0, len(nums)-1
        
        while start+1<end:
            mid = start+(end-start)//2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            first = start
        elif nums[end] == target:
            first = end
            
        start, end = 0, len(nums)-1
        while start+1<end:
            mid = start+(end-start)//2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            last = end
        elif nums[start] == target:
            last = start
        
        return [first,last]
            