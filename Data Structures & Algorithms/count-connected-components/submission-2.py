class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = n
        par = [i for i in range(n)]
        rank = [1]*n

        def find(v):
            p = par[v]
            while p!=par[p]:
                p = par[par[p]]
                p=par[p]
            return p
        def union(v1,v2):
            p1,p2 = find(v1),find(v2)
            
            if p1==p2:
                return
            nonlocal comp
            comp -= 1
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1] += rank[p2]
            else:
                par[p1]= p2
                rank[p2] += rank[p1]
        for v1,v2 in edges:
            union(v1,v2)
        return comp

