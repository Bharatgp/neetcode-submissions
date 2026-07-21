class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curset, res = [] , []
        nums.sort()

        def helper(i,curset,res,nums):
            if i == len(nums):
                res.append(curset.copy())
                return
            curset.append(nums[i])
            helper(i+1,curset,res,nums)
            curset.pop()
            while i+1< len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1,curset,res,nums)
        helper(0,curset,res,nums)
        return res