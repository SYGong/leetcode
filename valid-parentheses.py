class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }

        stack = []
        # Go to https://siyuangong.com/projects/#leetcode for other
        # solutions, analysis and updates. 

        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack or pairs[stack.pop()] != c:
                return False
        return not stack