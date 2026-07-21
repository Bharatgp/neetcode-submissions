class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(n+1)}

        for u,v,t in times:
            adj[u].append((t,v))
        
        heap = [(0,k)]

        visit = set()

        t = 0 
        
        while heap:
            w,n1 = heapq.heappop(heap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t,w)

            for time, des in adj[n1]:
                if des not in visit:
                    heapq.heappush(heap, (w+time,des) )
        return t if len(visit)==n else -1


