class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+","-","*","/")
        for c in tokens:
            if c in operators:
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                if c == "+":
                    stack.append(v1+v2)
                elif c == "-":
                    stack.append(v2-v1)
                elif c == "*":
                    stack.append(v2*v1)
                else:
                    stack.append(v2/v1)
            else:
                stack.append(c)
        return int(stack[-1])