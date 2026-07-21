class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset,result = [],[]
        
        def helper(i, nums, currset, result):
            if i == len(nums):
                result.append(currset.copy())
                return
            currset.append(nums[i])
            helper(i+1,nums,currset,result)

            currset.pop()
            helper(i+1,nums,currset,result)
        helper(0,nums,currset,result)            
        return result
        