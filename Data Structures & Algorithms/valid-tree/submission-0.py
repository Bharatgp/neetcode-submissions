class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n : return False
        par = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(node):
            parent = par[node]
            while parent != par[parent]:
                parent = par[parent]
            return parent
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2 : return 0

            if  rank[p1] > rank[p2]:
                par[p2]=p1
                rank[p1] += rank[p2]
            else:
                par[p1]= p2
                rank[p2] += rank[p1]
            return 1

        for n1,n2 in edges:
            components -= union(n1,n2)
        print(components)
        return True if components == 1 else False                                                                    
