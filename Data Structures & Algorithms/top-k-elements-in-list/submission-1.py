class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        buckets = [[] for i in range(len(nums)+1)]
        for n in nums:
            ht[n] = 1 + ht.get(n,0)
        for n,c in ht.items():
            buckets[c].append(n)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:            
                res.append(num)
                if len(res)==k:
                    return res



