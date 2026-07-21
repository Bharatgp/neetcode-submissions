class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currMin = prices[0]

        for i in prices[1:]:
            if i<currMin:
                currMin = i
            else:
                maxProfit = max(maxProfit,i-currMin)

        return maxProfit 
