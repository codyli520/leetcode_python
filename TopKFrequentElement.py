class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numbers = {}
        for n in nums:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1
        
        freq = {}
        for key,v in numbers.items():
            if v in freq:
                freq[v].append(key)
            else:
                freq[v] = [key]
        
        res = []
        for i in range(len(nums),0,-1):
            if i in freq:
                for val in freq[i]:
                    res.append(val)

        return res[:k]
        