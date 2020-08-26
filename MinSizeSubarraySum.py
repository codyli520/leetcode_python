class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        left = 0
        right = 0

        if not nums:
            return 0

        min_len = len(nums) + 1

        nums_sum = 0

        for right in range(len(nums)):
            nums_sum += nums[right]
            while nums_sum >= s:
                min_len = min(min_len, right - left + 1)
                nums_sum -= nums[left]
                left += 1

        if min_len == len(nums) + 1:
            return 0
        return min_len
