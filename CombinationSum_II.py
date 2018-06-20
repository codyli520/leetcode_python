class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.dfs([],candidates,0, target, result)
        return result

    def dfs(self, subset, candidates, index, target, result):
    	if target == 0 and subset not in result:
    		result.append(subset)
    		return

    	for i in range(index, len(candidates)):
    		if candidates[i] > target:
    			continue
    		self.dfs(subset+[candidates[i]],candidates,i+1, target-candidates[i],result)