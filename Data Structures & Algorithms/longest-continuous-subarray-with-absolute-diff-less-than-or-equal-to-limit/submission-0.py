class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()

        l = 0 
        res = 0
        for r in range(len(nums)):
            #Maxq 
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            
            maxQ.append(nums[r])
            minQ.append(nums[r])

            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                if minQ[0] == nums[l]:
                    minQ.popleft()
                l+=1
            
            res = max(res,r-l+1)
        return res