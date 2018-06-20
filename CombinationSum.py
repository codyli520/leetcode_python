class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        if candidates[0] <= target:
            self.dfs([],candidates,0,target,result,)
        return result
    
    def dfs(self,subset, candidates,index, target, result):
        if target == 0:
            result.append(subset)
            return
            
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                continue
            if target - candidates[i] >= 0:
                self.dfs(subset+[candidates[i]],candidates,i, target-candidates[i],result)