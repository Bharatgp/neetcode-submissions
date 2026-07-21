class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree =[0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res = []
        while q:
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr not in res:
                    res.append(curr)
                for nei in adj[curr]:
                    indegree[nei] -= 1
                    if indegree[nei]==0:
                        q.append(nei)
        return res if len(res) == numCourses else []


