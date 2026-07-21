class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {n : [] for n in range(numCourses)}
        indegree = [0]*numCourses
        for crs, preq in prerequisites:
            adj[preq].append(crs)
            indegree[crs] += 1
        q = collections.deque()
        res = []
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                res.append(i)
        
        while q:
            currCourse = q.popleft()

            for dependents in adj[currCourse]:
                indegree[dependents] -= 1
                if indegree[dependents] ==0 :
                    res.append(dependents)
                    q.append(dependents)
        return len(res)==numCourses
        