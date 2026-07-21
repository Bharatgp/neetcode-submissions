class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ds = set()

        for i in nums:
            if i in ds:
                return True
            ds.add(i)
        return False            