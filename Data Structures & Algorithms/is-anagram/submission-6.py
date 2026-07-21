class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht = {}
        for i in s:
            ht[i] = 1 + ht.get(i,0)
        for i in t:
            if i not in ht:
                return False
            ht[i] -= 1
            if ht[i]==0: del ht[i]
        
        return True if len(ht) == 0 else False