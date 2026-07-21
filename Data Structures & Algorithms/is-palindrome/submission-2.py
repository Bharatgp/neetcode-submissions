class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNumeric(c):
            if ord(c) >= ord('a') and ord(c) <=ord('z'):
                return True
            elif ord(c) >= ord('A') and ord(c) <=ord('Z'):                 
                return True
            elif ord(c) >= ord('0') and ord(c) <=ord('9'):
                return True
            else:
                return False     

        s= s.replace(" ","").lower()
        temp = ""
        for i in s:
            if isAlphaNumeric(i):
                temp += i
        
        r,l = len(temp)-1,0

        while(r>=l):
            if(temp[r]!=temp[l]):
                return False
            r -= 1
            l += 1
        return True                                            


                                   