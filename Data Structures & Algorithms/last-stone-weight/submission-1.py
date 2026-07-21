class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nl = [-s for s in stones]
        heapq.heapify(nl)
        while len(nl)>1:
            first = nl[0]
            heapq.heappop(nl)
            second = nl[0]
            heapq.heappop(nl)
            if (first != second):
                heapq.heappush(nl,first-second)
        if len(nl) == 0:
            return 0
        return -nl[0]                            
