class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        for i in range(len(nums)):
            ht = {}
            a = nums[i]
            target = -a 
            for j in range(i+1, len(nums)):
                diff = target - nums[j]

                if diff in ht and ht[diff]!= 0:
                    ht[diff] -= 1
                    res.add(tuple(sorted([a, nums[j], diff])))
                ht[nums[j]] = 1 + ht.get(nums[j],0)
        return [list(t) for t in res]
