class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        if len(nums) == len(n):
            return False
        return True