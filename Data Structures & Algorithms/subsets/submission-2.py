class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_set = []

        def subsets(i):
            if i == len(nums):
                res.append(curr_set.copy())
                return
            #include i
            curr_set.append(nums[i])
            subsets(i+1)
            curr_set.pop()
            subsets(i+1)
        subsets(0)            
        return res                


