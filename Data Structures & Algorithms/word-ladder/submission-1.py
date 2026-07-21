class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = {w: [] for w in wordList}

        def checkDiff(s1, s2):
            if len(s1) != len(s2):
                return False
            count = 0
            for c1, c2 in zip(s1, s2):  # Use zip to pair up characters from both strings
                if c1 != c2:
                    count += 1
                if count > 1:
                    return False
            return count == 1  # Must differ by exactly one character

        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if checkDiff(wordList[i],wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        visited = set()

        q = collections.deque()

        q.append(beginWord)
        visited.add(beginWord)
        distance = 1
        while q:
            qlen = len(q)
            distance+=1
            for i in range(qlen):
                currNode = q.popleft()
                for nei in adj[currNode]:
                    if nei == endWord:
                        return distance
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        return 0