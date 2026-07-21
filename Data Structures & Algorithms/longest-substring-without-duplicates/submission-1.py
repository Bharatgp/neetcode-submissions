class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currChars = set()
        maxWindow = 0
        l,r = 0,0
        
        while(l<=r and r<len(s)):
            if s[r] not in currChars:
                currChars.add(s[r])
                r+=1
            else:
                while l<=r and s[r] in currChars:
                    currChars.remove(s[l])
                    l+=1
                    
            maxWindow = max(maxWindow, r-l)
        return maxWindow
            

