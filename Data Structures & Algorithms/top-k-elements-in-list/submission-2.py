class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums)+1

        buckets = [[] for _ in range(max_freq)]
        freq_ht = {}
        for i in nums:
            freq_ht[i] = 1 + freq_ht.get(i,0)

        for n,c in freq_ht.items():
            buckets[c].append(n)            
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                k = k-1
                if k == 0:
                    return res
                    

        