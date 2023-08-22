class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            
        return max_area