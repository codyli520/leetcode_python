class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        largest_sum = [0] * len(nums)
        largest_sum[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + largest_sum[i - 1] > nums[i]:
                largest_sum[i] = nums[i] + largest_sum[i - 1]
            else:
                largest_sum[i] = nums[i]

            res = max(res, largest_sum[i])

        return res

