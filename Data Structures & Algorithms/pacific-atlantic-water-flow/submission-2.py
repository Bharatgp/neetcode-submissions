class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])

        pacific = set()
        atlantic = set()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        pq = collections.deque()
        aq = collections.deque()

        for r in range(rows):
            pacific.add((r,0))
            pq.append((r,0))
            atlantic.add((r,cols-1))
            aq.append((r,cols-1))
        for c in range(cols):
            pacific.add((0,c))
            pq.append((0,c))
            atlantic.add((rows-1,c))
            aq.append((rows-1,c))


        def bfs(q,s):

            if not q: return

            while q:
                qLen = len(q)
                for i in range(qLen):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        nr,nc = r+dr, c+dc
                        if not (nr<0 or nr>= rows or nc<0 or nc>= cols or (nr,nc) in s or heights[r][c] > heights[nr][nc]):
                            s.add((nr,nc))
                            q.append((nr,nc))
        bfs(aq,atlantic)
        print(sorted(atlantic))
        bfs(pq,pacific)
        print(sorted(pacific))

        res = atlantic & pacific

        return [[i,j] for i,j in res]


               

