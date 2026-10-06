class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for t in tokens:
            if t in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b
                else:
                    result = int(a/b)
                stack.append(result)
            else:
                stack.append(t)
        return stack[-1]