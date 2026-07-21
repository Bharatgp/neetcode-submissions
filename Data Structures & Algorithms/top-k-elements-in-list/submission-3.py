class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        res = [[] for i in range(len(nums) + 1)]
        for n in nums:
            ht[n] = ht.get(n,0) + 1
        
        for key,value in ht.items():
            res[value].append(key)
        op = []
        for i in range(len(res)-1,0,-1):
            for num in res[i]:
               op.append(num)
               if len(op) == k:
                return op

