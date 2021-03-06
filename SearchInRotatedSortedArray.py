class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target is None:
            return -1
        
        start, end = 0, len(nums)-1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[start] < nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1