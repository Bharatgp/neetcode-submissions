class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            #for odd length
            l,r = i,i
            cnt_odd=0
            while(l>=0 and r<len(s) and l<=r and s[l]==s[r]):
                cnt_odd += 1 
                l -=1
                r +=1
            l,r = i,i+1
            cnt_even = 0
            while(l>=0 and r<len(s) and l<=r and s[l]==s[r]):
                cnt_even += 1 
                l -=1
                r +=1
            res = res + cnt_odd + cnt_even
        return res            