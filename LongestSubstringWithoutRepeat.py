class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        substring = ""

        for char in s:
            if char not in substring:
                substring += char
            else:
                while char in substring:
                    substring = substring[1:]
                substring += char
            res = max(res, len(substring))

        return res
