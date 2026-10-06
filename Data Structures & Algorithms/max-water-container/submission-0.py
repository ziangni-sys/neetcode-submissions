class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = min(heights[i], heights[j]) * (j - i)
        max_area = area
        while i != j:
            if heights[i] > heights[j]:
                j = j - 1
                area = min(heights[i], heights[j]) * (j - i)
                max_area = max(max_area, area)
            else:
                i = i + 1
                area = min(heights[i], heights[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area                