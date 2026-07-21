class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i,n in enumerate(nums):
            key = target - n

            if key in my_map:
                return[my_map[key],i]
            
            if n not in my_map:
                my_map[n]=i
        return []
