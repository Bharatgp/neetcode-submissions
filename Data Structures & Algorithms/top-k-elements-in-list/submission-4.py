class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        l = [[] for i in range(len(nums) + 1)]
        for i in nums:
            counter[i] = 1 + counter.get(i,0)

        for k1,v in counter.items():
            l[v].append(k1)
        op = []
        for i in range(len(l)-1,0,-1):
            for j in l[i]:
                op.append(j)
                if len(op)==k:
                    return op
        