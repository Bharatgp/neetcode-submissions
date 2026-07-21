class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curset,res = [] , []
        candidates.sort()
        
        def helper(i,candidates,curset,res,target,cur_sum):
            if cur_sum == target:
                res.append(curset.copy())
                return
            if cur_sum > target or i >= len(candidates):
                return
            curset.append(candidates[i])
            print(curset)
            helper(i+1,candidates,curset,res,target,cur_sum+candidates[i])
            curset.pop()
            while i + 1 < len(candidates) and candidates[i]==candidates[i+1]:
                i=i+1
            
            helper(i+1,candidates,curset,res,target,cur_sum)

        helper(0,candidates,curset,res,target,0)

        return res
        