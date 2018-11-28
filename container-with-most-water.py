class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # https://leetcode.com/articles/container-with-most-water/#approach-2-two-pointer-approach
        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            max_vol = max(min(height[l], height[r]) * (r - l), max_vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_vol