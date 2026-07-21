class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        def cal(piles,k):
            res =0
            for i in piles:
                res += math.ceil(float(i)/k)
            return res                
        while low <= high:
            mid = low + ((high-low)//2)
            if(cal(piles,mid) <= h):
                high = mid -1 
                ans = min(ans,mid)
            elif(cal(piles,mid) > h):
                low = mid + 1
        return ans                