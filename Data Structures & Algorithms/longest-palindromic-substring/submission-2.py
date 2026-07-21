class Solution:
    def longestPalindrome(self, s: str) -> str:
        lgstPalin = 0
        lgstStr = ""
        if not s : 
            return lgstPalin

        for i in range(len(s)):
            #odd case
            l, r  = i,i
            while l>=0 and r<len(s) and (s[l]==s[r]):
                currlen = r - l + 1     
                if lgstPalin < currlen:
                    lgstStr = s[l:r+1]
                    lgstPalin = currlen
                l -= 1
                r += 1
            #even case
            l, r  = i,i+1
            while l>=0 and r<len(s) and (s[l]==s[r]):
                currlen = r - l + 1     
                if lgstPalin < currlen:
                    lgstStr = s[l:r+1]
                    lgstPalin = currlen
                l -= 1
                r += 1
        return lgstStr
