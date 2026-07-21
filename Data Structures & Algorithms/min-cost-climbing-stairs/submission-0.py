class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        two = cost[len(cost)-1]
        one = cost[len(cost)-2]

        for i in range(len(cost)-3,-1,-1):
            prev_one = one
            one = cost[i]+ min(prev_one,two)
            two = prev_one
        return min(one,two)            
