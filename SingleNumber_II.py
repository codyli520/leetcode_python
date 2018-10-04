class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expect_sum = 3*sum(set(nums))
        real_sum = sum(nums)
        
        res = (expect_sum - real_sum)//2
        
        return res
        