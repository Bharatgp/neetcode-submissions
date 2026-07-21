class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht1 = {}
        ht2 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            ht1[s[i]] =1+ ht1.get(s[i],0)
            ht2[t[i]] = 1+ht2.get(t[i],0)
        return ht1==ht2            

