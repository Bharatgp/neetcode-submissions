class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        
        for i, n in enumerate(nums):
            ht[n]=i

        for i, n in enumerate(nums):
            diff = target-n
            if diff in ht and ht[diff]!=i:
                return [i,ht[diff]]




