class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights) 
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                right[j] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        triple = list(zip(left,right,heights))
        max_term = max(triple, key=lambda x : (x[1] - x[0] - 1) * x[2])
        return (lambda x : (x[1] - x[0] - 1) * x[2])(max_term)