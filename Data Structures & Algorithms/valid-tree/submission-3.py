class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1]*n
        comp = n
        def find(v):
            p = par[v]
            while p!=par[p]:
                p=par[p]
            return p
        def union(v1,v2):
            p1,p2 = find(v1),find(v2)

            if p1==p2:
                return False
            nonlocal comp
            comp -= 1
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for v1,v2 in edges:
            if not union(v1,v2):
                return False
        return comp == 1