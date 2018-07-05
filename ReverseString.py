class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        size =len(s)
        
        for i in range(0,size/2):
            s[i],s[size-1-i] = s[size-1-i],s[i]
        
        return "".join(s)