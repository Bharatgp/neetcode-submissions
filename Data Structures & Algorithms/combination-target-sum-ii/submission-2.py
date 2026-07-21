class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def dfs(i,sm):
            if sm == target:
                res.append(curr.copy())
                return
            if sm > target:
                return                
            if i == len(candidates):
                return                

            curr.append(candidates[i])
            dfs(i+1,sm+candidates[i])
            curr.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sm) 
        dfs(0,0)            
        return res                             
