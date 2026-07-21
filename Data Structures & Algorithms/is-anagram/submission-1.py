class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtab1 = {}
        hashtab2 = {}
        if len(s) != len(t): return False

        for i,j in zip(s,t):
            hashtab1[i] = hashtab1.get(i,0) + 1
            hashtab2[j] = hashtab2.get(j,0) + 1
        return hashtab1 == hashtab2