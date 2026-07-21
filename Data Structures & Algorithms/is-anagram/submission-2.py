class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasttab = {}

        if len(s)!= len(t): return False

        for i in s:
            hasttab[i] = 1 + hasttab.get(i,0)
        for j in t:
            if hasttab.get(j,0) == 0:
                return False
            hasttab[j] -=  1
        return True
                    

        