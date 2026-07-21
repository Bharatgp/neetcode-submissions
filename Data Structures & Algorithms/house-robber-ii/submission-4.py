class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def robHelper(cost):
            if len(cost)==0:
                return 0
            dp = [0]*(len(cost)+1)
            dp[1] = cost[0]
            for i in range(2,len(cost)+1):
                dp[i] = max(cost[i-1]+dp[i-2],dp[i-1])
            return dp[-1]

        return max(robHelper(nums[1:]),robHelper(nums[:-1]))