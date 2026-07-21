class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]

        stack = []
        ind = 0
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                index = stack.pop()
                res[index[1]] = i - index[1]
            stack.append((n,i))                        
        return res                                                    