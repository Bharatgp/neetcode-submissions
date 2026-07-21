class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        s = []

        def dfs(dig):
            if len(dig)==0:
                if(len(s)>0):
                    res.append(''.join(s.copy()))
                return
            for i in range(len(digitToChar[dig[0]])):
                s.append(digitToChar[dig[0]][i])
                dfs(dig[1:])
                s.pop()
        dfs(digits)
        return res                    
