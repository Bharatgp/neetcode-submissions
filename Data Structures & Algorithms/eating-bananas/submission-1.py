class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        def cal(k):
            time = 0
            for i in piles:
                time+=math.ceil(i/k)
            return time                
        while l<=r:
            mid = l+(r-l)//2
            if(cal(mid)<=h):
                res = min(res,mid)
                r = mid - 1                
            else:
                l = mid + 1
        return res                                