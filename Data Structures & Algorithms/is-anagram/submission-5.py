class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = [0]*26
        

        for char in s:
            st[ord(char)-ord('a')] +=1
        
        for char in t:
            st[ord(char)-ord('a')] -= 1
        
        for i in st:
            if i!=0: 
                return False
        return True
        
        