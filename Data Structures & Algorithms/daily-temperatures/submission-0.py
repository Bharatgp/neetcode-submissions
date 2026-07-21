class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]

        stack = []
        ind = 0
        for i,n in enumerate(temperatures):
            if not stack:
                stack.append((n,i))
            else:                
                if stack[-1][0] >= n:
                    stack.append((n,i))
                else:
                    k = 0
                    while stack and n > stack[-1][0]:
                        k+=1
                        index = stack.pop()
                        res[index[1]] = i - index[1]
                    stack.append((n,i))                        
        return res                                                    