class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i,n in enumerate(nums):
            target = -n
            ht = {}
            for j,nj in enumerate(nums[i+1:]):
                diff = target - nj
                if diff in ht:
                    res.add(tuple(sorted([n,nj,diff])))
                ht[nj] = j
        return [list(k) for k in res]                                                    

