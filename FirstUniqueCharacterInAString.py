class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        for i,v in enumerate(s):
            if v in res:
                res[v] = -1
            else:
                res[v] = i
        
        ans = len(s)+1
        for k in res:
            if res[k] != -1:
                if ans > res[k]:
                    ans = res[k]
        
        if ans == len(s)+1:
            return -1
        return ans
        