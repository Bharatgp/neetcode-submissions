class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_ht = [0] * 26
        t_ht = [0] * 26
        print(s_ht)
        for i in s:
            s_ht[ord(i)-ord('a')] += 1

        for i in t:
            t_ht[ord(i)-ord('a')] += 1                                

        for i in range(26):
            if s_ht[i]!=t_ht[i]:
                return False
        return True                            