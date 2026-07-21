class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currset, result =[], []

        def helper(i,nums,currset,result,target,cur_sum):                
            if cur_sum == target:
                result.append(currset.copy())
                return
            if cur_sum > target:
                return
            if i == len(nums):
                return
            currset.append(nums[i])
            helper(i,nums,currset,result,target,cur_sum+nums[i])
            currset.pop()
            helper(i+1,nums,currset,result,target,cur_sum)


        helper(0,nums,currset,result,target,0)

        return result
