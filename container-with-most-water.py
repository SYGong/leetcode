class Solution:
    def maxArea(self, height):
        area, left, right, mx = 0, 0, len(height) - 1, max(height)
        while left < right:
            if mx * (right - left) < area: break
            lv, rv = height[left], height[right]
            width = right - left
            if lv < rv:
                if (width*lv) > area: area = width*lv
                while height[left] <= lv:
                    left += 1
            else:
                if (width*rv) > area: area = width*rv
                while height[right] <= rv and right:
                    right -= 1
        return area