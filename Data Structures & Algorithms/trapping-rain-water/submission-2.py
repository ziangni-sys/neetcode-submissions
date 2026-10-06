class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        all_water = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if stack:
                    water = (min(height[stack[-1]], height[i]) - height[top]) * (i - stack[-1] - 1)                
                    all_water += water
            stack.append(i)
        return all_water