class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i,n in enumerate(nums):
            x = target - n
            if x not in ht:
                ht[n]=i
            else:
                return ([ ht[x],i ])
        return None
