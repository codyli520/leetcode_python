class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if nums[abs(n)] < 0 :
                return abs(n)
            else:
                nums[abs(n)] = -nums[abs(n)]
        return -1