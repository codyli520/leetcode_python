class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def hasOverlap(a1, a2, b1, b2):
            return (a1 < b2 and a2 > b1)

        return hasOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and hasOverlap(rec1[1], rec1[3], rec2[1], rec2[3])