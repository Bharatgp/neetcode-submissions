class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for crs,pre in prerequisites:
            indegree[crs]+=1
            adj[pre].append(crs)

        q = deque()
        finish = 0

        for i in range(numCourses):
            if(indegree[i]==0):
                q.append(i)

        res = []
        while q:
            cur = q.popleft()
            finish += 1
            res.append(cur)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if(indegree[nei]==0):
                    q.append(nei)
        return res if numCourses == finish else []