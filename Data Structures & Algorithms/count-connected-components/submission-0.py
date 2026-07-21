class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for i in range(n) ]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        components = 0
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for nei in adj[node]:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components +=1
        return components


