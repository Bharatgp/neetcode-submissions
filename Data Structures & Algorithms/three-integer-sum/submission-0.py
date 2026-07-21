class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if(nums[i]+nums[l]+nums[r]==0):
                    res.append([nums[i],nums[l],nums[r]])
                    r = r -1 
                    while nums[r]==nums[r+1] and r > l:
                        r -= 1
                    
                elif(nums[i]+nums[l]+nums[r] > 0):
                    r -= 1
                else:
                    l += 1
        return res
