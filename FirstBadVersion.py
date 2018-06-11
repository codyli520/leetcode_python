# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None:
            return -1
        
        start, end = 1, n
        
        while start + 1 < end:
            mid = start + (end - start)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
        return -1