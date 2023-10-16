class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_v = 0
        while l < r:
            y = min(height[l], height[r])
            max_v = max(max_v, y*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1 
        return max_v
