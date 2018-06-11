class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        deleted = ''
        while B not in A:
            deleted = B[-1]+deleted
            B = B[:-1]
        
        if deleted in A:
            return True
        return False
        
# if len(A) > len(B):
#             return False
        
#         A = A * 2
        
#         return B in A