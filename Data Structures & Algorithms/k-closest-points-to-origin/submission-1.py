class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_pts = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(dis_pts)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dis_pts)[1])
        return res