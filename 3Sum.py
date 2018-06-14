class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums:
            return result
        nums.sort()
        
        for x in range(len(nums)):
            # 如果x大于0，且nums的x位置和x-1位置值相等，跳过以避免重复
            if x>0 and nums[x] == nums[x-1]:
                continue
            y = x+1
            z = len(nums)-1

            while y<z:
                if nums[x]+nums[y]+nums[z] > 0:
                    z -= 1
                elif nums[x]+nums[y]+nums[z] < 0:
                    y += 1
                elif nums[x]+nums[y]+nums[z] == 0:
                    result.append([nums[x],nums[y],nums[z]])
                    
                    # 跳过相等的值
                    while y<z and nums[y] == nums[y+1]:
                        y+=1
                    while y<z and nums[z] == nums[z-1]:
                        z-=1
                        
                    # y位置和z位置不会再用到，更新
                    y += 1
                    z -=1
                
        return result