class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        
        for i,num in enumerate(nums):
            dif = target - num

            if dif in ht:
                return [ht[dif],i]
            ht[num] = i
        