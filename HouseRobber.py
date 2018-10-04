class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or not nums:
        	return 0

        stash = [0, nums[0]]
        max_money = nums[0]

        for i in range(1,len(nums)):
        	stash.append(max(stash[i+1-2]+nums[i], stash[i+1-1]))
        return stash[-1]
