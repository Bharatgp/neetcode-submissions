class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i,n in enumerate(nums):
            target = -n
            ht = {}
            for j in range(i+1,len(nums)):
                dif = target - nums[j]

                if dif in ht:
                    res.add(tuple(sorted([n,dif,nums[j]])))
                ht[nums[j]] = j
        
        return [list(k) for k in res]



                

