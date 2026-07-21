class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right,left = 1,0
        curSum = nums[0]
        res = curSum
        while right<len(nums):
            if(nums[right]+curSum > nums[right]):
                curSum+=nums[right]
                right+=1
            else:
                left = right
                curSum=nums[right]
                right+=1
            res = max(res,curSum)
        return res
