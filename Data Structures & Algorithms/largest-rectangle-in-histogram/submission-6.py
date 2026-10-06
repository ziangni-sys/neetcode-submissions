class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                right[j] = i
            if stack:    
                left[i] = stack[-1]
            stack.append(i)
        
        return max(( r - l - 1 ) * heights[i] for r, l, i in zip(right, left, range(n)))
        