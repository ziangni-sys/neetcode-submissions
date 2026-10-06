class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
                while stack and stack[-1][1] < t:
                    a = stack.pop()
                    k = a[0]
                    output[k] = i - k 
                stack.append((i,t))
        return output