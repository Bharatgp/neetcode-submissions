class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curset, res = [] , []
        visited = []
        for i in range(len(nums)):
            visited.append(False)
        def helper(curset,res,nums,visited):
            if len(curset) == len(nums):
                res.append(curset.copy())
                return
            for i in range(len(nums)):
                if visited[i]==False:
                    curset.append(nums[i])
                    visited[i]=True
                    helper(curset,res,nums,visited.copy())
                    visited[i]=False
                    curset.pop()
        helper(curset,res,nums,visited)
        return res
        